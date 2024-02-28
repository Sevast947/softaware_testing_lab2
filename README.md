# softaware_testing_lab2

[![Coverage Status](https://coveralls.io/repos/github/Sevast947/softaware_testing_lab2/badge.svg?branch=main)](https://coveralls.io/github/Sevast947/softaware_testing_lab2?branch=main)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Sevast947_softaware_testing_lab2&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=Sevast947_softaware_testing_lab2)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=Sevast947_softaware_testing_lab2&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=Sevast947_softaware_testing_lab2)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=Sevast947_softaware_testing_lab2&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=Sevast947_softaware_testing_lab2)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=Sevast947_softaware_testing_lab2&metric=bugs)](https://sonarcloud.io/summary/new_code?id=Sevast947_softaware_testing_lab2)

# План тестирования:

<ol>
  <li>
    <h4>Тест А1: Положительный - Поиск товара по названию</h4>
    <ul>
      <li>Начальное состояние: Программа запущена, пользовательский интерфейс ожидает ввода.</li>
      <li>Действие: Пользователь запрашивает поиск товаров по названию "Bread" через метод get_items_by_title класса Shop.</li>
      <li>Ожидаемый результат: Возвращается непустой список экземпляров товаров с названием "Bread".</li>
    </ul>
  </li>
  <li>
    <h4>Тест А2: Положительный - Применение скидки на товар</h4>
    <ul>
      <li>Начальное состояние: Начальные данные загружены в систему, скидки отсутствуют.</li>
      <li>Действие: Создание экземпляра класса DiscountManager и вызов метода define_discount для установки скидки 25% на комикс с id "11111".</li>
      <li>Ожидаемый результат: Скидка применена успешно, цена товара снижается с 7.99 до 5.99.</li>
    </ul>
  </li>
  <li>
    <h4>Тест А3: Негативный - Добавление товара с дублирующим id</h4>
    <ul>
      <li>Начальное состояние: В системе уже есть комикс с id "12345".</li>
      <li>Действие: Попытка добавления второго комикса с тем же id "12345" с использованием метода add_item класса Shop.</li>
      <li>Ожидаемый результат: Выдача ошибки с кодом DuplicateIdError, указывающей на дублирование id.</li>
    </ul>
  </li>
  <li>
    <h4>Тест А4: Негативный - Попытка продать товар, которого нет в наличии</h4>
    <ul>
      <li>Начальное состояние: Товар с указанным id отсутствует в инвентаре или его количество равно нулю.</li>
      <li>Действие: Попытка продажи комикса с нулевым остатком с использованием метода sell_item класса Shop.</li>
      <li>Ожидаемый результат: Выдача ошибки с кодом IdNotInStockError, указывающей на отсутствие товара на складе.</li>
    </ul>
  </li>
</ol>
<ol>
  <li>
    <h4>Тест А5: Положительный — Поиск товара по производителю</h4>
    <ul>
      <li>Начальное состояние: Программа запущена, товары загружены в систему.</li>
      <li>Действие: Пользователь запрашивает поиск товаров по производителю "Glass Factory" с помощью метода get_items_by_manufacturer.</li>
      <li>Ожидаемый результат: Возврат списка всех товаров, производителем которых является "Glass Factory".</li>
    </ul>
  </li>
  <li>
    <h4>Тест А6: Негативный — Поиск товара по id, которого нет в системе</h4>
    <ul>
      <li>Начальное состояние: Программа запущена, комиксы загружены в систему.</li>
      <li>Действие: Пользователь пытается найти товар с несуществующим id 99999 через метод get_items_by_id.</li>
      <li>Ожидаемый результат: Выдача ошибки ItemNotFoundError, указывающей на отсутствие товара с таким id.</li>
    </ul>
  </li>
  <li>
    <h4>Тест А7: Положительный — Отображение всех товаров в наличии</h4>
    <ul>
      <li>Начальное состояние: Программа запущена, товары загружены в систему.</li>
      <li>Действие: Вызов метода display_inventory класса Shop.</li>
      <li>Ожидаемый результат: Пользователю показывается список всех товаров в наличии.</li>
    </ul>
  </li>

<ol>
  <li>
    <h4>Тест Б1: Положительный - Создание объекта Item</h4>
    <ul>
      <li>Название: Создание объекта Item.</li>
      <li>Действие: Инициализация экземпляра класса Item с валидными параметрами.</li>
      <li>Ожидаемый результат: Объект успешно создан с заданными свойствами.</li>
    </ul>
  </li>
  <ol>
  <li>
    <h4>Тест Б2: Положительный - Обновление количества товаров в инвентаре</h4>
    <ul>
      <li>Название: Обновление количества товаров в инвентаре.</li>
      <li>Действие: Вызов метода update_inventory с положительным числом для экземпляра Item.</li>
      <li>Ожидаемый результат: Количество в инвентаре обновлено на указанное значение.</li>
    </ul>
  </li>
    </ol>
  <ol>
  <li>
    <h4>Тест Б3: Негативный - Попытка установить отрицательное количество товаров</h4>
    <ul>
      <li>Название: Установка отрицательного количества товаров.</li>
      <li>Действие: Инициализация экземпляра класса Item с отрицательным значением количества.</li>
      <li>Ожидаемый результат: Выбрасывается исключение NegativeInventoryError.</li>
    </ul>
  </li>
  </ol>
  <li>
    <h4>Тест Б4: Положительный - Удаление товара из магазина</h4>
    <ul>
      <li>Название: Успешное удаление товара.</li>
      <li>Действие: Вызов метода remove_item для удаления существующего комикса из инвентаря магазина.</li>
      <li>Ожидаемый результат: товар удалён, попытка доступа к товару по id возвращает ошибку ItemNotFoundError.</li>
    </ul>
  </li>
  <li>
    <h4>Тест Б5: Положительный - Редактирование информации товара</h4>
    <ul>
      <li>Название: Изменение информации о товаре.</li>
      <li>Действие: Вызов метода edit_items_info для существующего товара с передачей новых значений свойств.</li>
      <li>Ожидаемый результат: Значения свойств товара успешно обновлены.</li>
    </ul>
  </li>
</ol>
  <li>
    <h4>Тест Б6: Негативный — Создание объекта Item с отрицательной ценой</h4>
    <ul>
      <li>Название: Недопустимая цена товара.</li>
      <li>Действие: Инициализация экземпляра класса Item с отрицательной ценой.</li>
      <li>Ожидаемый результат: Вызов исключения InvalidPriceError.</li>
    </ul>
  </li>
  
</ol>
<ol> 
<li>
<h4>Тест И1: Положительный - Взаимодействие классов Shpo и Item при добавлении и продаже товара</h4> 
<ul> 
<li>Название: Процесс добавления товара в магазин и его продажа.</li> 
<li>Действие: Создание экземпляра Item и его добавление в Shop с помощью метода add_item, затем продажа комикса с помощью метода sell_item.</li> 
<li>Ожидаемый результат: Уменьшение количества экземпляров Item в Shop на один после продажи.</li> 
</ul> 
</li> 
<li>
<h4>Тест И2: Положительный - Проверка интеграции Shop и DiscountManager при установке скидки и продаже товара</h4> 
<ul> 
<li>Название: Устанавливаем скидку на товар и проверяем цену при его продаже.</li> 
<li>Действие: Установка скидки на комикс через DiscountManager и выполнение продажи этого товара с учетом скидки через Shop.</li> 
<li>Ожидаемый результат: Цена товара должна уменьшиться в соответствии с установленной скидкой на момент продажи.</li> 
</ul> 
</li> 
<li>
<h4>Тест И3: Положительный - Проверка ошибок при попытке установить скидку для ненайденного товара</h4> 
<ul> 
<li>Название: Ошибка при установке скидки на несуществующий товар.</li> 
<li>Действие: Попытка установить скидку на комикс с id, которого нет в инвентаре Shop через DiscountManager.</li>
<li>Ожидаемый результат: Получение исключения ComicNotFoundError.</li> 
</ul> 
</li> 
<li>
<h4>Тест И4: Положительный - Проверка добавления и удаления товаров из Shop</h4> 
<ul> 
<li>Название: Добавление товара и его последующее удаление.</li> 
<li>Действие: Добавление экземпляра Item в Shop и удаление его из инвентаря магазина.</li> 
<li>Ожидаемый результат: После удаления товара он больше не доступен в Shop.</li> 
</ul> 
</li> 
<li>
<h4>Тест И5: Положительный - Проверка обновления информации о товаре через методы Shop</h4> 
<ul> 
<li>Название: Обновление информации о товаре в Shop.</li> 
<li>Действие: Изменение свойств уже добавленного в магазин экземпляра Item (например, название, производитель или цена).</li> 
<li>Ожидаемый результат: Информация о товаре обновлена в соответствии с выполненными изменениями.</li> 
</ul> 
</li> 
<li>
    <h4>Тест И6: Положительный — Обновление инвентаря после продажи</h4>
    <ul>
      <li>Название: Уменьшение количества в инвентаре после продажи.</li>
      <li>Действие: Продажа одного экземпляра товара и автоматическое обновление инвентаря.</li>
      <li>Ожидаемый результат: Количество товара в инвентаре уменьшено на единицу после продажи.</li>
    </ul>
  </li>
</ol>
