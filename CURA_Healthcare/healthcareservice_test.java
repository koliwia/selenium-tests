import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class healthcareservice_test

{

    public static void main(String[] args)

    {

        System.setProperty("webdriver.chrome.driver", "C:/chromedriver.exe");

        WebDriver driver = new ChromeDriver();

// Logging in
        driver.get("https://katalon-demo-cura.herokuapp.com/");

        driver.findElement(By.id("btn-make-appointment")).click();

        driver.findElement(By.id("txt-username")).sendKeys("John Doe");

        driver.findElement(By.id("txt-password")).sendKeys("ThisIsNotAPassword");

                driver.findElement(By.id("btn-login")).click();


       boolean make_appointment = driver.findElement(By.cssSelector("#appointment > div > div > div > h2")).isDisplayed();
        Assert.assertEquals(true, make_appointment);

// Filling in the form
        driver.findElement(By.name("facility")).sendKeys("Hongkong CURA Healthcare Center");


// Clicking on the checkbox
        WebElement check_hospital_redmission = driver.findElement(By.id("chk_hospotal_readmission"));
        check_hospital_redmission.click();

// Choosing the healthcare program
        WebElement healthcare_program = driver.findElement(By.id("radio_program_medicaid"));
        healthcare_program.click();

//Selecting a visit date
        WebElement visit_form = driver.findElement(By.id("txt_visit_date"));
        visit_form.click();

//Selecting a month
        driver.findElement(By.xpath("//*/div[1]/table/thead/tr[2]/th[2]")).click();
        driver.findElement(By.xpath("//*/div[2]/table/tbody/tr/td/span[2]")).click();

//Selecting a day
        driver.findElement(By.xpath("//*/div[1]/table/tbody/tr[2]/td[4]")).click();

// Adding a comment
        driver.findElement(By.id("txt_comment")).sendKeys("ASAP");

// Booking an appointment
        WebElement bookingclick = driver.findElement(By.id("btn-book-appointment"));
        bookingclick.click();

// Appointment Confirmation is visible
        boolean appointment_confirmation = driver.findElement(By.cssSelector("#summary > div > div > div.col-xs-12.text-center > h2")).isDisplayed();
        Assert.assertEquals(true, appointment_confirmation);

// Logging out
        driver.findElement(By.id("menu-toggle")).click();

        driver.findElement(By.cssSelector("#sidebar-wrapper > ul > li:nth-child(6) > a")).click();

        driver.findElement(By.id("menu-toggle")).click();

        boolean login_button = driver.findElement(By.cssSelector("#sidebar-wrapper > ul > li:nth-child(4) > a")).isDisplayed();
        Assert.assertEquals(true, login_button);

        driver.quit();

    }
}