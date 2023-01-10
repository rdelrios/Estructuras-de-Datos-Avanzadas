 class Main {
   
    
  public static void main(String[] args) {
    Prueba p=new Prueba();
    MiLista<Integer> lista=new MiLista<Integer>();
    //p.f1(0);
    lista.inserta(1);
    lista.inserta(2);
    lista.inserta(3);
    lista.inserta(4);
    //lista.imprime();
    lista.imprimeAlrevez();
    System.out.println("recursivo");
    lista.imprimeR();
  

    
  }
}