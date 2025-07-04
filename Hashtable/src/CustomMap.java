import java.util.LinkedList;
import java.util.Iterator;

public class CustomMap<K,V> implements IMap<K,V> {
    private static class Entry<K,V> {
        final K key;
        V value;

        public Entry(K key, V value) {
            this.key = key;
            this.value = value;
        }
    }

    private LinkedList<Entry<K,V>>[] table; //Массив списков где хранятся элементы хеш-таблицы
    private int size; //Текущее количество элементов в таблице
    private static final int DEFAULT_CAPACITY = 16; //Размер таблицы по умолчанию
    private static final double LOAD_FACTOR = 0.75; //Коэффициент загрузки

    @SuppressWarnings("unchecked") //Подавляет предупреждение о непроверяемом приведении типов
    public CustomMap() {
        this.table = (LinkedList<Entry<K,V>>[]) new LinkedList[DEFAULT_CAPACITY];
        this.size = 0;
    }

    private int hash(K key) { //Вычисляет индекс корзины для ключа
        return key == null ? 0 : Math.abs(key.hashCode() % table.length);
    }

    @Override
    public void put(K key, V value) { //Проверяет, что ключ не null
        if (key == null) {
            throw new IllegalArgumentException("Key cannot be null");
        }

        int index = hash(key); //Вычисляет индекс корзины и создает новый связный список, если корзина пуста
        if (table[index] == null) {
            table[index] = new LinkedList<>();
        }

        for (Entry<K,V> entry : table[index]) { // // Проверяет, есть ли уже такой ключ в корзине
            if (entry.key.equals(key)) {
                entry.value = value; // Если находит - обновляет значение
                return;
            }
        }

        // Добавляет новую пару ключ-значение в корзину и увеличивает счетчик элементов
        table[index].add(new Entry<>(key, value));
        size++;

        // Проверяет необходимость расширения таблицы
        if ((double)size / table.length > LOAD_FACTOR) {
            resize();
        }
    }

    private void resize() { //Создает новую таблицу в 2 раза больше и сбрасывает счетчик элементов
        LinkedList<Entry<K,V>>[] oldTable = table;
        table = (LinkedList<Entry<K,V>>[]) new LinkedList[table.length * 2];
        size = 0;

        for (LinkedList<Entry<K,V>> bucket : oldTable) {
            if (bucket != null) {
                for (Entry<K,V> entry : bucket) {
                    put(entry.key, entry.value); // Перехэширование
                }
            }
        }
    }

    @Override
    public V get(K key) { // Ищет значение по ключу
        int index = hash(key);
        if (table[index] != null) {
            for (Entry<K,V> entry : table[index]) {
                if (entry.key.equals(key)) {
                    return entry.value;
                }
            }
        }
        return null;
    }

    @Override
    public void remove(K key) { //Удаляет элемент по ключу
        int index = hash(key);
        if (table[index] != null) {
            Iterator<Entry<K,V>> iterator = table[index].iterator();
            while (iterator.hasNext()) {
                Entry<K,V> entry = iterator.next();
                if (entry.key.equals(key)) {
                    iterator.remove();
                    size--;
                    return;
                }
            }
        }
    }

    @Override
    public boolean containsKey(K key) { // Проверяет наличие ключа в таблице (но возвращает boolean)
        int index = hash(key);
        if (table[index] != null) {
            for (Entry<K,V> entry : table[index]) {
                if (entry.key.equals(key)) {
                    return true;
                }
            }
        }
        return false;
    }

    @Override
    public int size() { //Возвращает текущее количество элементов в таблице
        return size;
    }

    @Override
    public void clear() { // Очищает таблицу
        for (int i = 0; i < table.length; i++) {
            table[i] = null;
        }
        size = 0;
    }
}