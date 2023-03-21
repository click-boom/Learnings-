class vehicle {
    int passengers; // number of passnegers
    int fuelcap; // fuel cappacity in gallons
    int mpg; // fuel consumption in miles per gallon
}

class vehicledemo {
    public static void main(String[] args) {
        vehicle minivan = new vehicle();
        minivan.passengers= 30;
        minivan.fuelcap = 20;
        minivan.mpg = 23;

        System.out.println("Range:"+ (minivan.fuelcap* minivan.mpg));
    }
}