封裝 Encapsulation
=====
* public：public表明該資料成員、成員函式是對所有使用者開放，所有使用者都可以直接進行呼叫
* private：private表示私有，私有的意思就是除了class自己之外，任何人都不可以直接使用，私有財產神聖不可侵犯嘛，即便是子女，朋友，都不可以使用。
* protected：protected對於子女、朋友來說，就是public的，可以自由使用，沒有任何限制，而對於其他的外部class，protected就變成private。


            | Class | Package | Subclass | Subclass | World
            |       |         |(same pkg)|(diff pkg)|
————————————+———————+—————————+——————————+——————————+————————
public      |   √   |    √    |    √     |     √    |   √
————————————+———————+—————————+——————————+——————————+————————
protected   |   √   |    √    |    √     |     √    |
————————————+———————+—————————+——————————+——————————+————————
no modifier |   √   |    √    |    √     |          |
————————————+———————+—————————+——————————+——————————+————————
private     |   √   |         |          |          |


Overloading 重載/多載
=====
```java
static int binarySearch(byte[] a, byte key);
static int binarySearch(byte[] a, int fromIndex, int toIndex, byte key);
```

Overriding 子類別覆寫
=====
```java
class Animal{
    protected int legs = 1;
    public int getLegs(){
      return legs*4;
    }
}
class Bird extends Animal{
   public int getLegs(){
       return legs*2;
   }
}
```

final 常數
=====
* 跟 C 的 const 是一樣的

Abstract class
=====
* 僅宣告方法名稱而不實作當中的邏輯，這樣的方法稱之為「抽象方法」（Abstract method），
* 如果一個類別中包括了抽象方法，則該類別稱之為「抽象類別」（Abstract class）
```java
public abstract class Listener {
    double PI = 3.14149; // 同public static final
    protected abstract void showMessage(String message); // 同public abstract
}
public class A implements Listener {
    protected void showMessage(String message) {
        System.out.println(message + "!");
    }
}
```

Interface 界面
=====
```java
public interface Listener {
    double PI = 3.14149; // 同public static final
    void listen(); // 同public abstract
}
public class A implements Listener {
    public void listen() {
    }
}
```

generic 泛型
=====
```java
List<Integer> intList = new LinkedList<Integer>();
List<Double> intList = new LinkedList<Double>();
```

Polymorphism 多型
=====
```java
Animal puppy1, puppy2, puppy3; // Animal 宣告
puppy1 = new Elephant("大象", 6, 70); // new Elephant
```

Binding
=====
* Early (or static) binding = compile time binding
* Late (or dynamic) binding = runtime binding
```java
//early binding:
public create_a_foo(*args) {
    return new Foo(args)
}
my_foo = create_a_foo();

//late binding:
public create_something(Class klass, *args) {
    klass.new_instance(args)
}
my_foo = create_something(Foo);
```

Sort
=====
```java
List list = new ArrayList(coll);
Collections.sort(list);
```

Closure: Basics
=====
* {} 大括號為界定範圍
* 使用 => 箭頭分隔輸入和輸出
* 左邊是宣告參數的型別和變數名，逗點隔開，沒有則留白
* 右邊是 statement block，可以多個，最後一行可寫 expression，然後直接回傳值
```java
//類比的 AIC：
new Block() {
    public int sum(int x, int y) {
        System.out.println("some msg...");
        return x + y ;
    }
};

//對應的 closure 寫法
{ int x, int y => //參數列
    System.out.println("some msg..."); //中間可以多個 statement
    x + y //最後一行可以是 expression，不用寫 return
}
```

Closure: string to int
=====
```java
//原本 Java 的寫法
public List<Integer> convertStringToInteger(List<String> strings) {
    List<Integer> ints = new ArrayList<Integer>();
    for(String s : strings) {
       ints.add(Integer.parseInt(s));
    }
    return ints;
}

//改成 Closure:
public List<Integer> convertStringToInteger(List<String> strings) {
    return Collections.convert(strings, {String s => Integer.parseInt(s) });
}
```

Closure: InputStream
=====
```java
//原本 Java 的寫法
public void readData(InputStream inputStream) throws IOException{
    try {
        readFromInput(inputStream); //這個 method throws IOException
    } finally {
        try {
            if(inputStream !=null) {
                inputStream.close();
            }
        } catch (IOException ignore) {}
    }
}

//改成 Closure:
public void readData(InputStream inputStream) throws IOException {
    IO.with(inputStream, { InputStream in =>
       readFromInput(in) ; //這個 method throws IOException
    });
}
```
