import logging
from flask import Flask, request, jsonify
from db.models import db, Delivery
from utils.db_utils import init_db
import os
from sqlalchemy import URL

url_object = URL.create(
    "postgresql",
    username="user",
    password="password",  # plain (unescaped) text
    host="db",
    database="orders",
    port=5454
)
# Настройка логирования
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)


# Получение URL базы данных из переменной окружения
database_url = os.environ.get('DATABASE_URL')
logger.debug(f"Подключение к базе данных по адресу: {url_object}")
app.config['SQLALCHEMY_DATABASE_URI'] = url_object

# Инициализация базы данных
try:
    db.init_app(app)
    logger.info("Инициализация базы данных прошла успешно.")
except Exception as e:
    logger.error(f"Ошибка инициализации базы данных: {str(e)}")

# Маршрут для создания новой доставки
@app.route('/deliveries', methods=['POST'])
def create_delivery():
    data = request.get_json()
    logger.debug(f"Получены данные для создания доставки: {data}")
    try:
        new_delivery = Delivery(order_id=data['order_id'], status='In Transit')
        db.session.add(new_delivery)
        db.session.commit()
        logger.info(f"Доставка с номером заказа {data['order_id']} успешно создана.")
        return jsonify({'message': 'Delivery created successfully'}), 201
    except Exception as e:
        logger.error(f"Ошибка создания доставки: {str(e)}")
        return jsonify({'message': 'Error creating delivery'}), 500

# Маршрут для обновления статуса доставки
@app.route('/deliveries/<int:delivery_id>', methods=['PUT'])
def update_delivery(delivery_id):
    data = request.get_json()
    logger.debug(f"Получены данные для обновления доставки {delivery_id}: {data}")
    try:
        delivery = Delivery.query.get(delivery_id)
        if not delivery:
            logger.warning(f"Доставка с ID {delivery_id} не найдена.")
            return jsonify({'message': 'Delivery not found'}), 404

        delivery.status = data['status']
        db.session.commit()
        logger.info(f"Доставка с ID {delivery_id} успешно обновлена.")
        return jsonify({'message': 'Delivery updated successfully'})
    except Exception as e:
        logger.error(f"Ошибка обновления доставки с ID {delivery_id}: {str(e)}")
        return jsonify({'message': 'Error updating delivery'}), 500

if __name__ == '__main__':
    # Попытка инициализировать базу данных
    with app.app_context():
        try:
            init_db()
            logger.info("База данных успешно инициализирована.")
        except Exception as e:
            logger.error(f"Ошибка инициализации базы данных при запуске: {str(e)}")

    # Запуск приложения
    try:
        app.run(host='0.0.0.0', port=5001)
        logger.info("Приложение запущено на порту 5001.")
    except Exception as e:
        logger.error(f"Ошибка при запуске приложения: {str(e)}")