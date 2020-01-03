package fraction;

import org.junit.Assert;
import org.junit.jupiter.api.Test;

import static org.hamcrest.CoreMatchers.is;
import static org.hamcrest.MatcherAssert.assertThat;

class FractionTest {

       Fraction test_fraction_1 = new Fraction(8,3);
       Fraction test_fraction_2 = new Fraction(2, 4);
       Fraction test_fraction_3 = new Fraction(13,6);
       Fraction test_fraction_4 = new Fraction(19, 6);
       Fraction test_fraction_5 = new Fraction(4,3);
       Fraction test_fraction_6 = new Fraction(-8, -3);
       Fraction test_fraction_7 = new Fraction(-2, -4);
       Fraction test_fraction_8 = new Fraction(1,2);
       Fraction test_fraction_9 = new Fraction(12,1);
       Fraction test_fraction_10 = new Fraction(0,0);


    @Test
    void throwsException() {
        try {
            Fraction test_fraction10 = new Fraction(2, 0);
        }
        catch (ArithmeticException e) {
            assertThat("* assertion error not thrown *", e.getMessage(), is("Cannot use ZERO as denominator!"));
        }
    }


    @Test
    void add() {
        Fraction add_1 = test_fraction_1.add(test_fraction_2);
        Fraction add_2 = test_fraction_2.add(test_fraction_3);
        Fraction add_3 = test_fraction_6.add(test_fraction_1);
        Fraction add_4 = test_fraction_1.add(test_fraction_7);
        Fraction add_5 = test_fraction_7.add(test_fraction_6);

        Assert.assertEquals(" * Test for addition positives 1 failed * ", test_fraction_4, add_1);
        Assert.assertEquals(" * Test for addition positives 2 failed * ", test_fraction_1, add_2);
        Assert.assertEquals(" * Test for addition negative + positive failed * ", test_fraction_10, add_3);
        Assert.assertEquals(" * Test for addition positive + negative failed * ", new Fraction(13,6), add_4);
        Assert.assertEquals(" * Test for addition negative + negative failed * ", new Fraction(-19,-6), add_5);
    }


    @Test
    void subtract() {
        Fraction sub_1 = test_fraction_1.subtract(test_fraction_2);
        Fraction sub_2 = test_fraction_2.subtract(test_fraction_1);
        Fraction sub_3 = test_fraction_3.subtract(test_fraction_7);
        Fraction sub_4 = test_fraction_7.subtract(test_fraction_6);
        Fraction sub_5 = test_fraction_6.subtract(test_fraction_3);
        Assert.assertEquals("Test for subtraction1 failed", test_fraction_3, sub_1);
        Assert.assertEquals("Test for subtraction2 failed", test_fraction_3, sub_2);
        Assert.assertEquals("Test for subtraction negative from positive failed", test_fraction_1, sub_3);
        Assert.assertEquals("Test for subtraction negative from negative failed", test_fraction_3, sub_4);
        Assert.assertEquals("Test for subtraction positive from negative failed", new Fraction(-29,-6), sub_5);
    }


    @Test
    void multiply() {
        Fraction mult_1 = test_fraction_1.multiply(test_fraction_2);
        Fraction mult_2 = test_fraction_2.multiply(test_fraction_3);
        Fraction mult_3 = test_fraction_3.multiply(test_fraction_7);
        Fraction mult_4 = test_fraction_6.multiply(test_fraction_7);
        Fraction mult_5 = test_fraction_7.multiply(test_fraction_1);
        Assert.assertEquals(" * Test for multiplying positives 1 failed * ", test_fraction_5, mult_1);
        Assert.assertEquals(" * Test for multiplying positives 2 failed * ", new Fraction(13,12), mult_2);
        Assert.assertEquals(" * Test for multiplying positive with negative failed * ", new Fraction(-13,-12), mult_3);
        Assert.assertEquals(" * Test for multiplying negative with negative failed * ", test_fraction_5, mult_4);
        Assert.assertEquals(" * Test for multiplying negative and positive failed * ", new Fraction(-4,-3), mult_5);
    }


    @Test
    void divide() {
        Fraction div_1 = test_fraction_1.divide(test_fraction_2);
        Fraction div_2 = test_fraction_2.divide(test_fraction_3);
        Fraction div_3 = test_fraction_1.divide(test_fraction_6);
        Fraction div_4 = test_fraction_6.divide(test_fraction_3);
        Fraction div_5 = test_fraction_6.divide(test_fraction_7);
        Assert.assertEquals(" * Test for division positive/positive 1 failed * ",new Fraction(16,3), div_1);
        Assert.assertEquals(" * Test for division positive/positive 2 failed * ", new Fraction(3,13), div_2);
        Assert.assertEquals(" * Test for division positive/negative failed * ",  new Fraction(-1,-1), div_3);
        Assert.assertEquals(" * Test for division negative/positive failed * ", new Fraction(-16,-13), div_4);
        Assert.assertEquals(" * Test for division negative/negative failed * ", new Fraction(16,3), div_5);
    }


    @Test
    void abs() {
        Fraction abs_1 = test_fraction_6.abs();
        Fraction abs_2 = test_fraction_7.abs();
        Fraction abs_3 = test_fraction_1.abs();
        Assert.assertEquals(" * Test for negative abs1 failed * ",test_fraction_1, abs_1);
        Assert.assertEquals(" * Test for negative abs2 failed * ", test_fraction_2, abs_2);
        Assert.assertEquals(" * Test for positive abs2 failed * ", test_fraction_1, abs_3);
    }


    @Test
    void negate() {
        Fraction neg_1 = test_fraction_1.negate();
        Fraction neg_2 =  test_fraction_2.negate();
        Fraction neg_3 = test_fraction_6.negate();
        Fraction neg_4  = test_fraction_7.negate();
        Assert.assertEquals(" * Test for negate positive 1 failed * ",test_fraction_6 , neg_1);
        Assert.assertEquals(" * Test for negate positive 2 failed * ",test_fraction_7, neg_2);
        Assert.assertEquals(" * Test for negate negative 1 failed * ",test_fraction_1 , neg_3);
        Assert.assertEquals(" * Test for negate negative 2 failed * ",test_fraction_2, neg_4);
    }


    @Test
    void testEquals() {
        boolean eql_1 = test_fraction_1.equals(test_fraction_2) ;
        boolean eql_2 = test_fraction_2.equals(test_fraction_8);
        boolean eql_3 = test_fraction_1.equals(test_fraction_6);
        Assert.assertFalse(" * Test for different values (false) failed * ", eql_1);
        Assert.assertTrue(" * Test for equals same value different fraction failed * ", eql_2);
        Assert.assertFalse(" * Test for equal positive vs negative failed * ", eql_3);
    }


    @Test
    void inverse() {
        Fraction inv_1 = test_fraction_1.inverse();
        Fraction inv_2 = test_fraction_2.inverse();
        Fraction inv_3 = test_fraction_6.inverse();
        Fraction inv_4 = test_fraction_7.inverse();
        Assert.assertEquals(" * Test for inverse positive 1 failed * ",new Fraction(3,8), inv_1);
        Assert.assertEquals(" * Test for inverse positive 2 failed * ", new Fraction(2,1), inv_2);
        Assert.assertEquals(" * Test for inverse negative 1 failed * ", new Fraction(-3,-8), inv_3);
        Assert.assertEquals(" * Test for inverse negative 2 failed * ", new Fraction(-2,-1), inv_4);
    }


    @Test
    void compareTo() {
        int cmpr_1 = test_fraction_1.compareTo(test_fraction_2);
        int cmpr_2 = test_fraction_2.compareTo(test_fraction_3);
        int cmpr_3 = test_fraction_2.compareTo(test_fraction_8);
        Assert.assertEquals(" * Test for comparing higher failed * ",1, cmpr_1);
        Assert.assertEquals(" * Test for comparing lower failed * ",-1, cmpr_2);
        Assert.assertEquals(" * Test for comparing equal failed * ",0, cmpr_3);
    }


    @Test
    void testToString() {
        String to_str1 = test_fraction_1.toString();
        String to_str2 = test_fraction_6.toString();
        String str_1 = "8/3";
        String str_2 = "-8/3";
        Assert.assertEquals(" * Test for to string positive failed * ", str_1, to_str1);
        Assert.assertEquals("Test to string negative failed", str_2, to_str2 );
        Assert.assertEquals("Test to string where 1 failed", 12, test_fraction_9.toString());
    }
}
