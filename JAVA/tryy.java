
class Errorinfo {
    String[] msgs = {
            "Output Error",
            "Input Error",
            "Disk Full",
            "Index Out -Of-Bounds"
    };
    int[] howBad = { 3, 3, 2, 4 };

    Err getErrorinfo(int i) { // ( —— Return an object of type Err
        if (i >= 0 & i < msgs.length)
            return new Err(msgs[i], howBad[i]);
        else
            return new Err("Invalid Error Code", 0);
    }

}

class Err {
    String msg; // error message
    int severity; // code indicating severity of error

    Err(String m, int s) {
        msg = m;
        severity = s;
    }
}

public class tryy {

    public static void main(String[] args) {
        Errorinfo err = new Errorinfo();
        Err e;
        e = err.getErrorinfo(2);
        System.out.println(e.msg + " severity: " + e.severity);

        e = err.getErrorinfo(19);
        System.out.println(e.msg + " severity: " + e.severity);
    }
}