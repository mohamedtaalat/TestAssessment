from selenium.webdriver.common.by import By

from base.basis import Base


class Header(Base):
    def __init__(self, driver):
        super().__init__(driver)


    def click_services(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//a[@class='text-sm text-slate-300 transition hover:text-white'][normalize-space()='Services']"
        ).click()

    def click_about(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//a[@class='text-sm text-slate-300 transition hover:text-white'][normalize-space()='About']"
        ).click()


    def click_contact(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//a[@class='text-sm text-slate-300 transition hover:text-white'][normalize-space()='Contact']"
        ).click()

    def click_assessment(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//a[@class='text-sm text-slate-300 transition hover:text-white'][normalize-space()='Assessment']"
        ).click()

    def click_login(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//a[@class='hidden text-sm text-slate-300 hover:text-white sm:inline']"
        ).click()

    def click_open_account(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//a[@class='inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-md text-sm font-medium transition-all disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-4 shrink-0 [&_svg]:shrink-0 outline-none focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px] aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive h-9 px-4 py-2 has-[>svg]:px-3 bg-emerald-500 text-slate-950 hover:bg-emerald-400']"
        ).click()



