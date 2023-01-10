  public class Prueba{


    public void f5(int i){
      System.out.println(i);
      f5(i+1);
    }
    public void f4(int i){
      i=i+1;
      System.out.println(i);
   

    }
    public void f3(int i){
      i=i+1;
      System.out.println(i);
      f4(i);
      System.out.println(i);
    }

    public void f2(int i){
      i=i+1;
      System.out.println(i);
      f3(i);
      System.out.println(i);
    }


    public void f1(int i){
      System.out.println(i);
      f1(i);
      System.out.println(i);
    }

  }