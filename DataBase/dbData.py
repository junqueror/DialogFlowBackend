import logging
from DataBase.DataModels import *
from DataBase.DataModels.Enums import *


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

            # SmartPhones

            smartphone1 = SmartPhone(name='S9',
                                     company='Samsung',
                                     range=RangeEnum.High,
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
                                     imgURL='http://stg-images.samsung.com/is/image/samsung/p5/es/smartphones/galaxy-s9/gallery/s9plus_purple.png?$ORIGIN_PNG$'
                                     )

            smartphone2 = SmartPhone(name='G6',
                                     company='LG',
                                     range=RangeEnum.High,
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
                                     imgURL='https://images-na.ssl-images-amazon.com/images/I/81JyNh4wWuL._SL1500_.jpg'
                                     )

            smartphone3 = SmartPhone(name='Pixel 2',
                                     company='Google',
                                     range=RangeEnum.High,
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
                                     imgURL='https://i.blogs.es/36d8db/pixel-2-black-_-white-front-and-back/450_1000.jpg'
                                     )

            smartphone4 = SmartPhone(name='Xperia XZ1 Compact',
                                     company='Sony',
                                     range=RangeEnum.High,
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
                                     imgURL='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQdnslSefmaiohOgESwQC-jaJvXrKF4XIpXcx_qCZOfDF_SQAhm'
                                     )

            smartphone5 = SmartPhone(name='S8',
                                     company='Samsung',
                                     range=RangeEnum.High,
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
                                     imgURL='https://d243u7pon29hni.cloudfront.net/imagesOnDemand/get?imagePath=/images/products/samsung-gals8-5-8p4g8n64gb-negro-1360792_l.png&width=480&height=480&quality=65&imgType=product'
                                     )

            # Add to Database
            db.session.add(smartphone1)
            db.session.add(smartphone2)
            db.session.add(smartphone3)
            db.session.add(smartphone4)
            db.session.add(smartphone5)
            db.session.commit()
