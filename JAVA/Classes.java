class Vehicle{
    char name;
    int passengers ;
    int fuelcap;
    int mpg;
    int range;
    
    int range(){
        return(fuelcap*mpg);
    }
}
class Classes{
    public static void main(String a[]){
        Vehicle minivan=new Vehicle();
        Vehicle sportscar=new Vehicle();
        

        minivan.passengers=35;
        minivan.fuelcap=20;
        minivan.mpg=25;
        minivan.range= minivan.fuelcap*minivan.mpg;  //not used right now but can be used normally
        
        sportscar.passengers=1;
        sportscar.fuelcap=80;
        sportscar.mpg=110;
        sportscar.range= sportscar.fuelcap*sportscar.mpg;  //not used right now but can be used normally

        /* Using dynamic initialization */
        System.out.println("Capacity:"+ minivan.passengers+"Fuel:"+minivan.fuelcap+"Miles per gallon:"+minivan.mpg);
        System.out.println("Capacity:"+ sportscar.passengers+"Fuel:"+sportscar.fuelcap+"Miles per gallon:"+sportscar.mpg);

        /* Using method */
        System.out.println("minivan Range:"+minivan.range());
        System.out.println("sportscar Range:"+sportscar.range());

        Vehicle sedan=sportscar;
        Vehicle SUV= new Vehicle();
        SUV =sedan;
        
        System.out.println("Capacity:"+ SUV.passengers+"Fuel:"+sedan.fuelcap+"Miles per gallon:"+sportscar.mpg);  // all objects ultimately takes sportscar value
    }
}