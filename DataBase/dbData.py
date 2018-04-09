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

            eCommerce1 = Ecommerce(name='Amazon',
                                   URL='www.amazon.es',
                                   image='https://t2.uc.ltmcdn.com/images/5/2/0/img_como_comprar_en_amazon_desde_espana_24025_600.jpg')
            eCommerce2 = Ecommerce(name='Gearbest',
                                   URL='www.gearbest.es',
                                   image='data:image/png;base64,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')

            affiliateLink1 = AffiliateLink(link='link1',
                                           price=989,
                                           smartphoneId=1,
                                           ecommerceId=1)

            affiliateLink2 = AffiliateLink(link='link2',
                                           price=949,
                                           smartphoneId=1,
                                           ecommerceId=2)

            # Add to Database
            db.session.add(smartphone1)
            db.session.add(smartphone2)
            db.session.add(smartphone3)
            db.session.add(smartphone4)
            db.session.add(smartphone5)
            db.session.add(eCommerce1)
            db.session.add(eCommerce2)
            db.session.add(affiliateLink1)
            db.session.add(affiliateLink2)
            db.session.commit()
