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

    logging.info("Filling the DataBase...")
    logging.info("Filling the DataBase...")
    logging.info("Filling the DataBase...")

    @staticmethod
    def addtData(db, app):
        with app.app_context():
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

            # Ecommerces
            amazon = Ecommerce(name='Amazon',
                               URL='www.amazon.es',
                               image='https://t2.uc.ltmcdn.com/images/5/2/0/img_como_comprar_en_amazon_desde_espana_24025_600.jpg',
                               description='Mejor velocidad de envío y garantías de devolución',
                               rate=94)
            gearbest = Ecommerce(name='Gearbest',
                                 URL='www.gearbest.es',
                                 image='https://comprarchinobien.com/wp-content/uploads/2016/08/gearbest-espanol-ofertas.jpg',
                                 description='Buena oferta de productos chinos. Bajos precios, pero tiempos de envíos altos',
                                 rate=84)
            aliexpress = Ecommerce(name='AliExpress',
                                   URL='https://es.aliexpress.com',
                                   image='https://www.puntonegocio.com/images/easyblog_articles/500/maxresdefault.jpg',
                                   description='Precios bajos en tecnología. Sin garantías de devolución',
                                   rate=87)
            mediamarkt = Ecommerce(name='MediaMarkt',
                                   URL='https://www.mediamarkt.es/',
                                   image='https://cclasarenas.com/wp-content/uploads/2017/11/mediamarkt-las-arenas.jpg',
                                   description='Buenas ofertas temporales',
                                   rate=78)
            pccomponentes = Ecommerce(name='PCcomponentes',
                                      URL='https://www.pccomponentes.com/',
                                      image='http://s03.s3c.es/imag/_v0/770x420/2/9/1/pc-componentes.jpg',
                                      description='Ofertas semanales. Sin costes de envío',
                                      rate=83)
            db.session.add(amazon)
            db.session.add(gearbest)
            db.session.add(aliexpress)
            db.session.add(mediamarkt)
            db.session.add(pccomponentes)

            db.session.commit()

            # SmartPhones

            s9 = SmartPhone(name='S9',
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
                            extras='''micro-SD, NFC, carga rápida, carga inalámbrica, lector de huellas, escáner facial 
                            seguro, USB tipo C''',
                            officialURL='http://www.samsung.com/es/smartphones/galaxy-s9/camera/?cid=es_ppc_ds_S9warm_'
                                        'GOOGLE_ES_IM_S9_Brand_Awareness_Exact_RLSA_Warm_AO%20Samsung%20IM%20Smartphone'
                                        's_Brand_kw=samsung%20s9$$',
                            image='http://stg-images.samsung.com/is/image/samsung/p5/es/smartphones/galaxy-s9/gallery/'
                                  's9plus_purple.png?$ORIGIN_PNG$',
                            rate=88,
                            rateCamera=94,
                            rateScreen=95,
                            rateSoftware=86,
                            ratePerformance=87,
                            rateBattery=85)
            db.session.add(s9)
            db.session.commit()
            s9amazon = AffiliateLink(
                linkUrl='https://www.amazon.es/Samsung-Galaxy-Plus-Smartphone-Bluetooth/dp/B079XFR75F',
                price=904.86,
                smartphoneId=s9.id,
                ecommerceId=amazon.id)
            s9mediamarkt = AffiliateLink(
                linkUrl='https://tiendas.mediamarkt.es/p/movil-samsung-galaxy-s9-plus-6.2-violeta-1398572',
                price=892,
                smartphoneId=s9.id,
                ecommerceId=mediamarkt.id)
            s9pccomponentes = AffiliateLink(linkUrl='https://www.pccomponentes.com/samsung-galaxy-s9-purpura-libre',
                                            price=849,
                                            smartphoneId=s9.id,
                                            ecommerceId=pccomponentes.id)

            db.session.add(s9amazon)
            db.session.add(s9mediamarkt)
            db.session.add(s9pccomponentes)

            g6 = SmartPhone(name='G6',
                            company='LG',
                            rangeId=3,
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
                            image='https://images-na.ssl-images-amazon.com/images/I/81JyNh4wWuL._SL1500_.jpg',
                            rateCamera=91,
                            rateScreen=95,
                            rateSoftware=93,
                            ratePerformance=93,
                            rateBattery=90)
            db.session.add(g6)
            db.session.commit()
            g6pccomponentes = AffiliateLink(linkUrl='https://www.pccomponentes.com/lg-g6-32gb-plata-libre',
                                            price=429,
                                            smartphoneId=g6.id,
                                            ecommerceId=pccomponentes.id)
            db.session.add(g6pccomponentes)
            g6mediamarkt = AffiliateLink(
                linkUrl='https://tiendas.mediamarkt.es/p/movil-lg-g6-pantalla-5.7-qhd-camara-13mp-1360879',
                price=395,
                smartphoneId=g6.id,
                ecommerceId=mediamarkt.id)
            db.session.add(g6mediamarkt)
            g6amazon = AffiliateLink(
                linkUrl='https://www.amazon.es/LG-Smartphone-pantalla-pulgadas-Android/dp/B06XFRBM26/ref=sr_1_3?s=electronics&ie=UTF8&qid=1528564076&sr=1-3&keywords=lg%2Bg6&th=1',
                price=320,
                smartphoneId=g6.id,
                ecommerceId=amazon.id)
            db.session.add(g6amazon)

            pixel2 = SmartPhone(name='Pixel 2',
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
            db.session.add(pixel2)
            db.session.commit()
            pixel2amazon = AffiliateLink(
                linkUrl='https://www.amazon.es/Google-Pixel-%C3%BAnica-64GB-Negro/dp/B076KXR6C6/ref=sr_1_4?ie=UTF8&qid=1528565239&sr=8-4&keywords=google+pixel+2',
                price=655,
                smartphoneId=pixel2.id,
                ecommerceId=amazon.id)
            db.session.add(pixel2amazon)

            xperiaZ1compact = SmartPhone(name='Xperia XZ1 Compact',
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
            db.session.add(xperiaZ1compact)
            db.session.commit()

            s8 = SmartPhone(name='S8',
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
            db.session.add(s8)
            db.session.commit()

            RedmiNote4 = SmartPhone(name='Redmi Note 4',
                                    company='Xiaomi',
                                    rangeId=2,
                                    size='151 x 76 x 8.5 mm',
                                    weight='165g',
                                    screenSize='5.8"',
                                    screenType='IPS LCD',
                                    screenRes='1920 × 1080 px',
                                    processor='Snapdragon 625 ',
                                    RAM='3 GB',
                                    memory='32 GB',
                                    battery='4100 mAh',
                                    backCameraRes='13 Mpx',
                                    frontCameraRes='5 Mpx',
                                    OS='Android 6.0 Marshmallow + MIUI 8.1',
                                    extras='''micro-SD, NFC, Dual SIM LTE, WiFi 802.11 a/b/g/n, Bluetooth 4.2, WiFi Direct, GPS, radio FM, infrarrojo, minijack, MicroUSB''',
                                    officialURL='https://www.mi.com/es/note4/',
                                    image='https://d2giyh01gjb6fi.cloudfront.net/default/0001/58/thumb_57689_default_big.jpeg'
                                    )
            db.session.add(RedmiNote4)
            db.session.commit()
            redmiNote4amazon = AffiliateLink(
                linkUrl='https://www.amazon.es/Xiaomi-Redmi-Note-Smartphone-Android/dp/B074KRKGPD/ref=sr_1_2?ie=UTF8&qid=1528562645&sr=8-2&keywords=xiaomi+mi+note+4',
                price=159.90,
                smartphoneId=RedmiNote4.id,
                ecommerceId=3)
            db.session.add(redmiNote4amazon)

            onePlus6 = SmartPhone(name='6',
                                  company='One Plus',
                                  rangeId=4,
                                  size='155,7 x 75,4 x 7,75 mm',
                                  weight='177 ',
                                  screenSize='6.3"',
                                  screenType='AMOLED Gorilla Glass 5',
                                  screenRes='2280 x 1080 px',
                                  processor='Snapdragon 845',
                                  RAM='6 GB',
                                  memory='64 GB',
                                  battery='3300 mAh',
                                  backCameraRes='Doble 20/16 Mpx',
                                  frontCameraRes='16 Mpx',
                                  OS='OxygenOS basado en Android 8.1 Oreo',
                                  extras='''WiFi 802.11 a/b/g/n/ac, 2,4/5 GHz, MiMO 2x2, Bluetooth 5, LTE, NFC, GPS, GLONASS, BeiDou, Galileo, USB 2.0 de tipo C y soporte para Audio USB, Dual nano-SIM, jack 3,5 mm de audio''',
                                  officialURL='https://www.oneplus.com/es/6',
                                  image='https://image01.oneplus.net/shop/201805/31/625/f4a19f69328227f6988ece740e6fe5ee.jpg',
                                  rateCamera=85,
                                  rateScreen=90,
                                  rateSoftware=86,
                                  ratePerformance=97,
                                  rateBattery=82)
            db.session.add(onePlus6)
            db.session.commit()
            onePlus6amazon = AffiliateLink(
                linkUrl='https://www.amazon.es/OnePlus-Smartphone-Pantalla-Qualcomm-Snapgradon/dp/B07CK7KB95/ref=sr_1_4?s=electronics&ie=UTF8&qid=1528565948&sr=1-4&keywords=oneplus+6',
                price=619,
                smartphoneId=onePlus6.id,
                ecommerceId=amazon.id)
            db.session.add(onePlus6amazon)
            onePlus6eliexpress = AffiliateLink(
                linkUrl='https://es.aliexpress.com/store/product/Oneplus-6-4G-LTE-tel-fono-m-vil-6-28-6-GB-8-GB-RAM-64/2206089_32873918004.html?spm=a219c.search0204.3.6.354df373DLSwgJ&s=p&ws_ab_test=searchweb0_0,searchweb201602_2_10152_10151_10065_10344_10068_5722815_10342_10547_10343_10340_5722915_10548_10341_5722615_10696_10084_10083_10618_10307_10820_10301_10821_10303_5722715_10059_100031_10103_10624_10623_10622_5722515_10621_10620,searchweb201603_25,ppcSwitch_7_ppcChannel&priceBeautifyAB=0',
                price=486,
                smartphoneId=onePlus6.id,
                ecommerceId=aliexpress.id)
            db.session.add(onePlus6eliexpress)

            # Add to Database

            db.session.commit()

