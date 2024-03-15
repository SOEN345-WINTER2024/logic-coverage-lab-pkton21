import org.junit.*;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.OutputStream;
import java.io.PrintStream;

import static org.junit.Assert.*;


public class CheckItTest {
    private OutputStream os;
    private PrintStream ps;
    @Before
    public void init(){
        os = new ByteArrayOutputStream();
        ps = new PrintStream(os);
        System.setOut(ps);
    }

    @After
    public void reset(){
        PrintStream originalOut = System.out;
        System.setOut(originalOut);
    }
    @Test
    public void checkPCTrue(){
        CheckIt.checkIt(true, true, true);
        assertEquals("P is true\n", os.toString());
    }
    @Test
    public void checkPCFalse(){
        CheckIt.checkIt(false, false, false);
        assertEquals("P isn't true\n", os.toString());
    }

    @Test
    public void checkCCTrue(){
        CheckIt.checkIt(true, true, true);
        assertEquals("P is true\n", os.toString());
    }

    @Test
    public void checkCCFalse(){
        CheckIt.checkIt(false, false, false);
        assertEquals("P isn't true\n", os.toString());
    }

    @Test
    public void checkCACC(){
        CheckIt.checkIt(true, true, true);
        CheckIt.checkIt(false, false, true);
        assertEquals("P is true\n" +
                "P isn't true\n", os.toString());
    }

    @Test
    public void checkRACC(){
        CheckIt.checkIt(true, true, false); // P is true
        CheckIt.checkIt(false, true, false); // P is false
        assertEquals("P is true\n" +
                "P isn't true\n", os.toString()); // Checks both print statements
    }
}
