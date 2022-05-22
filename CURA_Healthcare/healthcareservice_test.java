import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class healthcareservice_test {
    public static void main(String[] args) {
        System.setProperty("webdriver.chrome.driver", "C:/chromedriver.exe");

        WebDriver driver = new ChromeDriver();

        // Logging in
        driver.get("https://katalon-demo-cura.herokuapp.com/");

        driver.findElement(By.id("btn-make-appointment")).click();

        driver.findElement(By.id("txt-username")).sendKeys("John Doe");

        driver.findElement(By.id("txt-password")).sendKeys("ThisIsNotAPassword");

        driver.findElement(By.id("btn-login")).click();

        boolean make_appointment = driver.findElement(By.cssSelector("#appointment > div > div > div > h2"))
                .isDisplayed();
        Assert.assertEquals(true, make_appointment);


        // Logging out
        driver.findElement(By.id("menu-toggle")).click();

        driver.findElement(By.cssSelector("#sidebar-wrapper > ul > li:nth-child(6) > a")).click();

        driver.findElement(By.id("menu-toggle")).click();

        boolean login_button = driver.findElement(By.cssSelector("#sidebar-wrapper > ul > li:nth-child(4) > a"))
                .isDisplayed();
        Assert.assertEquals(true, login_button);
    }
}