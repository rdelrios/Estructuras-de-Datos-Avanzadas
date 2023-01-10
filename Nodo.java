public class Nodo<T>{
  T elemento;
  Nodo<T> sig;
  Nodo(T elem){
    elemento=elem;
    sig=null;
  }
  public Nodo<T> getSig(){
    return sig;
  }
  public void setSig(Nodo<T> siguiente){
    sig=siguiente;
  }
  public void setElem(T elem){
    elemento=elem;
  }
  public T getElem(){
    return elemento;
  }
}