import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;

import java.util.Random;

public class WebDriverTest {
    // 需要安装webdriver https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/
    public static void main(String[] args) throws InterruptedException {
        System.setProperty("webdriver.chrome.driver","/Users/ymm/work/tools/webdriver/chromedriver");
       for(int i = 0; i < 1000; i++){
           WebDriver driver = new ChromeDriver();
           driver.get("https://blog.csdn.net/yang1210919685/article/details/122876692");
           wait(2);

           Actions actions = new Actions(driver);

           wait(3);
           // 页面滑动到底部
           actions.sendKeys(Keys.END).perform();
           wait(5);
           actions.sendKeys(Keys.HOME).perform();

           int magixX = new Random().nextInt(20);
           Thread.sleep((magixX + 1) * 1000);
           driver.quit();
       }
    }

    private static void wait(int sec) {
        try {
            Thread.sleep(sec * 1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
