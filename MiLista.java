





import java.util.Stack;

public class MiLista<T>{
  Nodo<T> cabeza;
  int cont;

  public MiLista(){
    cabeza= new Nodo<T>(null);
    cont=0;
  }
  public void inserta(T elem){
    Nodo<T> actual, nuevo=new Nodo<T>(elem);
    actual=cabeza;
    while(actual.getSig()!=null)
      actual=actual.getSig();

    actual.setSig(nuevo);
    cont++;
  }
    public void insertaMejor(T elem){
      Nodo<T> nuevo=new Nodo<T>(elem);
      nuevo.setSig(cabeza.getSig());
      cabeza.setSig(nuevo);
      cont++;   
    }
  
  public void imprime(){
    Nodo<T> actual;
    actual=cabeza.getSig();
    while(actual!=null){
      System.out.println(actual.getElem());
      actual=actual.getSig();
    }

  }
  public void imprimeAlrevez(){//con Stack
    Stack<T> pila=new Stack<T>();
    Nodo<T> actual=cabeza.getSig();

    while(actual!=null){
      pila.push(actual.getElem());
      actual=actual.getSig();
    }

    while(!pila.isEmpty())
      System.out.println(pila.pop());


  }
  public void imprimeR(){
    imprimeR(cabeza.getSig());
  }
  private void imprimeR(Nodo<T> actual){
    if (actual==null)
      return;

    //Si intercambio las siguientes dos lineas cambio de 
    //imprimir al derecho y alrevez el contenido de la MiLista
    //
    System.out.println(actual.getElem());
    imprimeR(actual.getSig());

  }


  
}