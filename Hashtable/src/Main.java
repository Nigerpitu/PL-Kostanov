
public class Main {
    public static void main(String[] args) {

        CustomMap<String,Integer> map=new CustomMap<>();
        map.put("Bracer",505);
        map.put("Disperser",6100);
        map.put("Satanic",5050);
        map.put("Nullifier",4375);
        map.put("Dagon",2800);

        System.out.println(map.containsKey("Disperser")); // Проверка наличия
        System.out.println(map.containsKey("Divine Rapier"));

        System.out.println(map.get("Dagon")); // Проверка значений

        System.out.println("Старая цена : " + map.get("Dagon")); // Обновление цен
        map.put("Dagon", 2850); // Нерф в новом патче
        System.out.println("Новая цена : " + map.get("Dagon"));

        System.out.println("\nПредметы с одинаковой ценой 2100:"); // Добавление предметов с одинаковой ценой
        map.put("Yasha", 2100);
        map.put("Kaya", 2100);
        map.put("Sange", 2100);
        System.out.println("Добавлено 3 предмета по 2100 золота");

        System.out.println("\nФинальная проверка цен:"); // Проверка всех добавленных значений
        String[] itemsToCheck = {
                "Bracer","Satanic","Dagon","Nullifier","Disperser","Yasha","Kaya","Sange"
        };

        for (String item : itemsToCheck) {
            System.out.printf("%-18s: %d%n", item, map.get(item));
        }

        System.out.println("Добавлено предметов: " + map.size()); // Проверка количества добавленных значений

        map.remove("Satanic"); // Удаление элемента

        System.out.println(map.get("Satanic"));

    }
}