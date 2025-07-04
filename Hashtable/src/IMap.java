public interface IMap<K,V> {

    void put(K key, V Value); // Добавление элемента

    V get(K key); // Получение значения по ключу

    void remove(K key); // Удаление элемента

    boolean containsKey(K key); // Проверка наличия ключа

    int size(); // Получение размера

    void clear(); // Очистка таблицы
}