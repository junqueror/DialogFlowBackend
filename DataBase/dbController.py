import logging
import traceback
from DataBase.dbWrapper import DbWrapper
from Utils.singleton import Singleton
from sqlalchemy import desc, or_, and_, inspect, asc
from sqlalchemy.sql.expression import cast
from sqlalchemy.dialects.mssql import VARCHAR


# Singleton class to make requests to de database

class DbController(DbWrapper, metaclass=Singleton):
    # Builds a new instance of DB if it is necessary
    def __init__(self):
        DbWrapper.__init__(self)

    def commitDB(self):
        self._db.session.commit()

    def getOne(self, model, ID):
        result = self._db.session.query(model).filter_by(id=ID).one()
        return result

    def getOneByName(self, model, name):
        result = self._db.session.query(model).filter(model.name.ilike(name)).one()
        return result

    def getOneByCompanyAndName(self, model, company, name):
        try:
            if company:
                result = self._db.session.query(model).filter(model.company.ilike(company)).filter(
                    model.name.ilike(name)).one()
            else:
                result = self._db.session.query(model).filter(model.name.ilike(name)).one()
        except:
            result = None
        return result

    def getCheapestOne(self, model, query=None):
        if not query:
            # Generate query on the model (model)
            query = self._db.session.query(model)

        result = query.order_by(asc(model.avgPrice)).limit(1).one()
        return result, query

    def getCheapests(self, model, number, query=None):
        if not query:
            # Generate query on the model (model)
            query = self._db.session.query(model)
        query = query.order_by(asc(model.avgPrice))
        results = query.limit(number).all()
        return results, query

    def getMostPowerful(self, model, number, query=None):
        if not query:
            # Generate query on the model (model)
            query = self._db.session.query(model)
        query = query.order_by(desc(model.RAM))
        results = query.limit(number).all()
        return results, query

    def getBestBattery(self, model, number, query=None):
        if not query:
            # Generate query on the model (model)
            query = self._db.session.query(model)
        query = query.order_by(desc(model.battery))
        results = query.limit(number).all()
        return results, query

    def getCheapestOneFilterBy(self, model, fields, search, query=None):

        if not query:
            # Generate query on the model (model)
            query = self._db.session.query(model)

        # Filtering
        filters = self._createFilters(search, fields, model, query)  # Build the appropriate filters for the query
        query = query.filter(or_(*filters))  # Apply filters to the query

        # Get the cheapest one
        result = query.order_by(asc(model.avgPrice)).limit(1).one()

        return result, query

    def getAll(self, model):
        results = self._db.session.query(model).all()
        return results

    def getAllFilterBy(self, model, search, fields=None, order=None, orderDir=None, query=None, number=None):

        results = None
        numResults = 0

        try:
            if not query:
                # Generate query on the model (model)
                query = self._db.session.query(model)

            # Filtering
            filters = self._createFilters(search, fields, model, query)  # Build the appropriate filters for the query
            query = query.filter(or_(*filters))  # Apply filters to the query

            # Sorting
            if order is None:
                query = query.order_by(model.getMainField())
            elif orderDir == 'desc':
                query = query.order_by(desc(getattr(model, order)))
            else:
                query = query.order_by(getattr(model, order))

            # In number of results specified
            query = query.limit(number)

            # Apply query and get the results
            results = query.all()

            # Count the number of total results
            numResults = query.count()

        except Exception as e:
            logging.error("searchFields ({0}): {1}".format(e, traceback.format_exc()))

        return results, query

    def _createFilters(self, search, fields, model, query):
        # Adjust the parameters for the filtering
        search = "%" + str(search) + "%"

        # Get the relations sub models and fields of the main model
        related_models, related_fields, related_fields_str = map(list, zip(*[(rel.mapper._identity_class,
                                                                              rel.class_attribute,
                                                                              str(rel.class_attribute))
                                                                             for rel in
                                                                             inspect(model).relationships]))
        # Get model fields to search
        modelFields = []
        if not fields or len(fields) == 0:  # If no fields defined
            for field in model.__table__.columns:
                modelFields.append(field)  # Filter in all fields of the table
            for field in related_fields:
                modelFields.append(field)  # And also filter in all fields related with other models
        else:
            for field in fields:
                modelFields.append(getattr(model, field))

        # Build the appropriate filter for the query
        filters = []
        for field in modelFields:

            # Check field type and add filter:
            if str(field) in related_fields_str:  # It is a relation field

                child = related_fields[related_fields_str.index(str(field))]
                childModel = related_models[related_fields_str.index(str(field))]

                mainFiled = childModel.getMainField()
                if str(mainFiled.type) == 'BOOLEAN':
                    pass  # Do not search in Boolean fields
                elif str(mainFiled.type) == 'VARCHAR':
                    query.join(child)
                    filters.append(child.any(mainFiled.ilike(search)))
                elif str(mainFiled.type) == 'INTEGER' or str(mainFiled.type) == 'DATETIME':
                    query.join(child)
                    filters.append(child.any(cast(mainFiled, VARCHAR).ilike(search)))
                else:
                    query.join(child)
                    filters.append(child.any(mainFiled == search))

            else:  # Not a relation field
                if str(field.type) == 'BOOLEAN':
                    pass  # Do not search in Boolean fields
                elif str(field.type) == 'VARCHAR' and field not in filters:
                    filters.append(field.ilike(search))
                elif (str(field.type) == 'INTEGER' or str(field.type) == 'DATETIME') and field not in filters:
                    # Type is integer OR DATE, search as a string
                    filters.append(cast(field, VARCHAR).ilike(search))
                elif field not in filters:
                    filters.append(field == search)
                else:
                    filters[field].append(field == search)

        return filters

    def delete(self, model, ID):
        result = self._db.session.query(model).filter_by(id=ID).delete(synchronize_session='fetch')
        self.commitDB()
        return True if result == 1 else False

    def add(self, object):
        self._db.session.add(object)
        self.commitDB()
        return True
