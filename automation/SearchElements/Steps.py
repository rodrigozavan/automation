from utils.Waits import Waits


class Steps:

    def __init__(self):
        self._waits = Waits.Wait()

    def search(self, driver):
        print(driver)
