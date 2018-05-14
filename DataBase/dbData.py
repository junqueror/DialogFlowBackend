import logging
from DataBase.DataModels import *


# Class to insert test data in the database
class DbData:
    @staticmethod
    def createTables(db, app):
        with app.app_context():
            logging.info("Rebuilding DataBase...")
            db.drop_all()
            db.create_all()

    @staticmethod
    def addtData(db, app):
        with app.app_context():
            logging.info("Filling the DataBase...")

            # Screens

            screen1 = Screen(name='Pantalla pequeña',
                             description='La gama baja es la única que puede optar por este tamaño de pantalla (menor de 5 pulgadas). Si buscas un móvil de tamaño reducido a costa de perder algo de resolución esta es tu opción. Suele conllevar un precio más reducido.',
                             minSize=None,
                             maxSize="5 pulgadas")
            screen2 = Screen(name='Pantalla mediana',
                             description='Es el tamaño de pantalla más habitual. Suele situarse en el rango de las 5 y 5.5 pulgadas. Es el tamaño que permite una mayor comodidad y tener una buena resolución al mismo tiempo. Si no deseas un terminal pequeño ásta es la opción que más recomendable.',
                             minSize="5 pulgadas",
                             maxSize="5.5 pulgadas")
            screen3 = Screen(name='Pantalla grande',
                             description='Pantallas de más de 5.5 pulgadas. Smarphones grandes, conocidos como Phablets. Ofrecen la mejor experiencia de visualización, calidad y resolución, a costa de penzalizar el consumo de batería y el precio del dispositivo',
                             minSize="5.5 pulgadas",
                             maxSize=None)
            db.session.add(screen1)
            db.session.add(screen2)
            db.session.add(screen3)

            range1 = Range(name='Gama baja',
                           description='Estos smartphones se centran en tener un precio muy reducido, a costa de ofrecer solo funcionalidades básicas. Si buscas un móvil solo para hablar por teléfono, chatear, navegación web, con una pantalla y dimensiones contenidas y sencillez de uso, ésta es tu opción.')
            range1.screens.append(screen1)
            range1.screens.append(screen2)
            range2 = Range(name='Gama media',
                           description='Smartphones con un buen rendimiento en la mayoría de las funciones habituales. Mejoran en cámara, pantalla y fluidez a los terminales de gama baja. Si buscas calidad-precio en términos generales es la mejor opción, pero si quieres utilizar muchas aplicacciones simultáneamente y jugar de vez en cuando tal vez debas elegir una gama superior.')
            range2.screens.append(screen2)
            range3 = Range(name='Gama alta',
                           description='Smartphones con un buen rendimiento en todos los aspectos. Cuentan con mejores procesadores y mayor cantidad de memoria, lo que les permite utilizar varias aplicaciones simultáneamente y ejecutar juegos con buena fluidez. Suelen contar con cámara de altas prestaciones y una pantalla de mejor calidad y resolución. Por contra, elevan su precio respecto a las gamas previas.')
            range3.screens.append(screen2)
            range3.screens.append(screen3)
            range4 = Range(name='Gama premium',
                           description='Los mejores smartphones del mercado. Los buques insignia de cada una de las marcas. Cuentan con las últimas tecnologías y destacan en prácticamente todos los aspectos. La mejor opción si haces un uso intensivo del móvil, juegas, utilizas todas las funcionalidades que puede ofrecerte, siempre que quieras y puedas pagar un precio más elevado.')
            range4.screens.append(screen2)
            range4.screens.append(screen3)

            db.session.add(range1)
            db.session.add(range2)
            db.session.add(range3)
            db.session.add(range4)

            # Update DB
            db.session.commit()

            # SmartPhones

            smartphone1 = SmartPhone(name='S9',
                                     company='Samsung',
                                     rangeId=4,
                                     size='147.3 × 68.5 × 8.3 mm',
                                     weight='164g',
                                     screenSize='5.8"',
                                     screenType='SuperAMOLED',
                                     screenRes='2960 × 1440 px',
                                     processor='Exynos 9810',
                                     RAM='4 GB',
                                     memory='64 GB',
                                     battery='3000 mAh',
                                     backCameraRes='12 Mpx',
                                     frontCameraRes='8 Mpx',
                                     OS='Android 8.0',
                                     extras='''micro-SD, NFC, carga rápida, carga inalámbrica, lector de huellas, escáner facial seguro, USB tipo C''',
                                     officialURL='http://www.samsung.com/es/smartphones/galaxy-s9/camera/?cid=es_ppc_ds_S9warm_GOOGLE_ES_IM_S9_Brand_Awareness_Exact_RLSA_Warm_AO%20Samsung%20IM%20Smartphones_Brand_kw=samsung%20s9$$',
                                     image='http://stg-images.samsung.com/is/image/samsung/p5/es/smartphones/galaxy-s9/gallery/s9plus_purple.png?$ORIGIN_PNG$'
                                     )

            smartphone2 = SmartPhone(name='G6',
                                     company='LG',
                                     rangeId=4,
                                     size='148.9 × 71.9 × 7.9 mm',
                                     weight='163 g',
                                     screenSize='5.7"',
                                     screenType=None,
                                     screenRes='2960 × 1440 px',
                                     processor='Snapdragon 821',
                                     RAM='4 GB',
                                     memory='32 GB',
                                     battery='3300 mAh',
                                     backCameraRes='13+13 Mpx',
                                     frontCameraRes='5 Mpx',
                                     OS='Android 7.1',
                                     extras='''micro-SD, NFC, carga rápida, lector de huellas, USB tipo C''',
                                     officialURL='http://www.lg.com/es/telefonos-moviles/lg-LGH870-black',
                                     image='https://images-na.ssl-images-amazon.com/images/I/81JyNh4wWuL._SL1500_.jpg'
                                     )

            smartphone3 = SmartPhone(name='Pixel 2',
                                     company='Google',
                                     rangeId=4,
                                     size='145.7 × 69.7 × 7.8 mm',
                                     weight='143 g',
                                     screenSize='5.0"',
                                     screenType='AMOLED',
                                     screenRes='1920 × 1080 px',
                                     processor='Snapdragon 835',
                                     RAM='4 GB',
                                     memory='64 GB',
                                     battery='2700 mAh',
                                     backCameraRes='12.2 Mpx',
                                     frontCameraRes='8 Mpx',
                                     OS='Android 8.0',
                                     extras='''NFC, carga rápida, lector de huellas, USB tipo C''',
                                     officialURL='https://www.android.com/phones/google-pixel-2/',
                                     image='https://i.blogs.es/36d8db/pixel-2-black-_-white-front-and-back/450_1000.jpg'
                                     )

            smartphone4 = SmartPhone(name='Xperia XZ1 Compact',
                                     company='Sony',
                                     rangeId=4,
                                     size='129 × 65 × 9.3 mm',
                                     weight='143 g',
                                     screenSize='5.8"',
                                     screenType='',
                                     screenRes='1280 × 720 px',
                                     processor='Snapdragon 835',
                                     RAM='4 GB',
                                     memory='32 GB',
                                     battery='2700 mAh',
                                     backCameraRes='19 Mpx',
                                     frontCameraRes='8 Mpx',
                                     OS='Android 8.0',
                                     extras='''micro-SD, NFC, carga rápida, lector de huellas, USB tipo C''',
                                     officialURL='',
                                     image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQdnslSefmaiohOgESwQC-jaJvXrKF4XIpXcx_qCZOfDF_SQAhm'
                                     )

            smartphone5 = SmartPhone(name='S8',
                                     company='Samsung',
                                     rangeId=4,
                                     size='148.9 × 68.1 × 8.0 mm',
                                     weight='155 g',
                                     screenSize='5.8"',
                                     screenType='',
                                     screenRes='2960 × 1440 px',
                                     processor='Exynos 8895',
                                     RAM='4 GB',
                                     memory='64 GB',
                                     battery='3000 mAh',
                                     backCameraRes='12 Mpx',
                                     frontCameraRes='8 Mpx',
                                     OS='Android 7.0',
                                     extras='''micro-SD, NFC, carga rápida, lector de huellas, USB tipo C''',
                                     officialURL='',
                                     image='https://d243u7pon29hni.cloudfront.net/imagesOnDemand/get?imagePath=/images/products/samsung-gals8-5-8p4g8n64gb-negro-1360792_l.png&width=480&height=480&quality=65&imgType=product'
                                     )

            db.session.add(smartphone1)
            db.session.add(smartphone2)
            db.session.add(smartphone3)
            db.session.add(smartphone4)
            db.session.add(smartphone5)

            eCommerce1 = Ecommerce(name='Amazon',
                                   URL='www.amazon.es',
                                   image='https://t2.uc.ltmcdn.com/images/5/2/0/img_como_comprar_en_amazon_desde_espana_24025_600.jpg',
                                   description='Mejor velocidad de envío y garantías de devolución',
                                   rate=92)
            eCommerce2 = Ecommerce(name='Gearbest',
                                   URL='www.gearbest.es',
                                   image='https://comprarchinobien.com/wp-content/uploads/2016/08/gearbest-espanol-ofertas.jpg',
                                   description='Buena oferta de productos chinos. Bajos precios, per tiempos de envíos altos',
                                   rate=84)
            eCommerce3 = Ecommerce(name='AliExpress',
                                   URL='https://es.aliexpress.com',
                                   image='https://www.puntonegocio.com/images/easyblog_articles/500/maxresdefault.jpg',
                                   description='Precios bajos en tecnología. Sin garantías de devolución',
                                   rate=84)
            db.session.add(eCommerce1)
            db.session.add(eCommerce2)
            db.session.add(eCommerce3)

            affiliateLink1 = AffiliateLink(linkUrl='link1',
                                           price=989,
                                           smartphoneId=1,
                                           ecommerceId=1)

            affiliateLink2 = AffiliateLink(linkUrl='link2',
                                           price=949,
                                           smartphoneId=1,
                                           ecommerceId=2)

            affiliateLink3 = AffiliateLink(linkUrl='link3',
                                           price=899,
                                           smartphoneId=1,
                                           ecommerceId=3)

            db.session.add(affiliateLink1)
            db.session.add(affiliateLink2)
            db.session.add(affiliateLink3)

            # Add to Database

            db.session.commit()
