import unittest
from coverage import Coverage

if __name__ == "__main__":

    omitPatterns = ['*tests*']

    # Setup the coverage object
    cov = Coverage(source=['API', 'Application', 'DataBase', 'External', 'Utils'], omit=omitPatterns, cover_pylib=False,
                   branch=True)
    cov.start()

    # Run unit tests
    testsDir = ''
    loader = unittest.TestLoader()
    suite = loader.discover(testsDir, pattern='test_*')
    runner = unittest.TextTestRunner()
    runner.run(suite)

    # Stop the coverage
    cov.stop()
    cov.save()

    # Create coverage reports
    print("\nCOVERAGE\n")
    cov.report()
    cov.html_report()
