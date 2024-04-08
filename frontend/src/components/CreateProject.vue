<template>
  <div class="main">
    <div class="overlay" v-if="showModal"></div>
    <div class="transition">
      <router-link to="/dashboard/project" class="eidt-link">Мои проекты</router-link>
      <div class="arrow-container">
        <img src="../../static/img/arrow-right.png" alt="Стрелка вправо" class="arrow-icon">
      </div>
      <p class="creation_text">Новый проект</p>
    </div>
    <div class="edit">
      <div class="head_container">
        <p class="header_text">Создание проекта</p>
        <p class="subheader_text">Название проекта не должно превышать 25 знаков</p>
      </div>
      <div class="form">
        <div class="form_container">
          <label for="">Название проекта</label>
          <input maxlength="25" type="text" placeholder="Введите название проекта" v-model="companyName">
          <p class="small-text">Для ввода доступно — <span class="remaining-characters">{{ remainingCharacters }}</span>/25</p>
        </div>
        <div class="form_container">
          <label for="service">Часовой пояс</label>
          <SelectPage
          :options="['0 — Лондон, Дублин', '+1 — Париж, Рим', '+2 — Афины, Каир', '+3 — Москва, Стамбул', '+4 — Дубай, Новосибирск', '+5 — Астана, Ташкент', '+6 — Омск, Бишкек', '+7 — Бангкок, Джакарта', '+8 — Гонконг, Сингапур', '-8 — Лос-Анджелес, Ванкувер', '-7 — Денвер, Эдмонтон', '-6 — Чикаго, Мехико', '-5 — Нью-Йорк, Монреаль', '-4 — Галифакс, Каракас', '-3 — Рио-де-Жанейро, Буэнос-Айрес']"
          @input="option => this.timezone = option"
          />
        </div>
        <div class="form_container">
          <label for="service">Валюта</label>
          <SelectPage
          :options="['RUB — Российский рубль', 'BYN — Белорусский рубль', 'USD — Доллар США', 'EUR — Евро', 'KZT — Казахстанский тенге', 'UAH — Украинская гривна', 'AZN — Азербайджанский манат', 'AMD — Армянский драм', 'GEL — Грузинский лари', 'KGS — Киргизский сом', 'TJS — Таджикский сомони', 'UZS — Узбекский сум', 'ARS — Аргентинское песо', 'BRL — Бразильский реал', 'AED — Дирхам ОАЭ', 'INR — Индийская рупи', 'MDL — Молдавский лей', 'NGN — Нигерийская найра', 'ILS — Новый израильский шекель', 'THB — Тайский бат', 'TRY — Турецкая лира ', 'ZAR — Южноафриканский рэнд']"
          @input="option => this.currency = option"
          />
        </div>
      </div>
      <div class="picker">
        <p class="color_text">Цвет иконки проекта</p>
        <div class="color_container">
          <div class="color" @click="this.color = '#F3F5F6'" style="background:#F3F5F6"></div>
          <div class="color" @click="this.color = '#7DCD37'" style="background:#7DCD37"></div>
          <div class="color" @click="this.color = '#28CCF0'" style="background:#28CCF0"></div>
          <div class="color" @click="this.color = '#9D8FF1'" style="background:#9D8FF1"></div>
          <div class="color" @click="this.color = '#FB88C0'" style="background:#FB88C0"></div>
          <div class="color" @click="this.color = '#F97F7F'" style="background:#F97F7F"></div>
          <div class="color" @click="this.color = '#F7D37D'" style="background:#F7D37D"></div>
        </div>
      </div>

      <div class="bottom">
        <div class="bottom_container">
          <button class="save" @click="save">Сохранить</button>
          <button class="back">Вернуться</button>
        </div>
        <button class="delete" @click="toggleModal">Удалить проект</button>
      </div>
    </div>
    <div v-if="showModal" class="modal">
      <div class="modal-content">
        <p class="text-header">Удаление проекта</p>
        <p class="modal-subtext">Вы действительно хотите удалить проект<span class="modal_span"> Барбершоп на Сатпаева?</span></p>
        <div class="btn_container">
          <button class="delete_edit" @click="deleteProject">Удалить</button>
          <button class="exit" @click="toggleModal">Отмена</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import SelectPage from '../components/SelectPage.vue';
import axios from 'axios';

export default {
  components: { SelectPage },
  data() {
    return {
      companyName: '',
      showModal: false,
      currency: '',
      timezone: '',
      color: '',
    };
  },
  computed: {
    remainingCharacters() {
      const maxLength = 25;
      return maxLength - this.companyName.length;
    },
  },
  methods: {
    toggleModal() {
      this.showModal = !this.showModal;
    },
    deleteProject() {
      // TODO: Ваш код для удаления проекта
      this.toggleModal();
    },
    save(){
      const data = {
      name: this.companyName,
      currency: this.currency,
      timezone: this.timezone,
      user_id: this.$store.state.registrationData.user_id,
      colour: this.color
    };

// Выполняем POST запрос с использованием Axios
axios.post('http://127.0.0.1:8000/api/create_project/', data)
  .then(response => {
    console.log('Успешно отправлено на сервер:', response.data);
    this.$router.push('/dashboard/project')
  })
  .catch(error => {
    console.error('Ошибка при отправке на сервер:', error);
  });    },
  },
};
</script>

<style scoped>
.transition {
  display: flex;
  flex-direction: row;
  gap: 10px;
  margin-bottom: 20px;
}
.eidt-link {
  font-family: TT Norms Medium;
  font-size: 20px;
  line-height: 24px;
  text-align: left;
  text-decoration: none;
  color: #AFB6C1;
}
.creation_text {
  color: #535C69;
  font-family: TT Norms Medium;
  font-size: 20px;
  line-height: 24px;
  letter-spacing: 0em;
  text-align: left;
  margin: 0;
}
.arrow-container {
  display: flex;
  align-items: center;
}
.arrow-icon {
  height: 50%;
}
.edit {
  width: 50%;
  height: auto;
  background-color: #FFFFFF;
  padding: 20px;
  border-radius: 5px;
  display: flex;
  flex-direction: column;
  gap: 20px;
}
.form{
  display: flex;
  flex-direction: column;
  gap: 20px;
}
.head_container{
  display: flex;
  flex-direction: column;
  gap: 5px;
}
.form_container{
  display: flex;
  flex-direction: column;
  gap: 5px;
}
.header_text{
  font-family: TT Norms Medium;
  font-size: 18px;
  line-height: 21px;
  letter-spacing: 0em;
  text-align: left;
  color: #535C69;
  margin: 0;
}
.subheader_text{
  font-family: TT Norms Medium;
  font-size: 14px;
  font-weight: 500;
  line-height: 17px;
  letter-spacing: 0em;
  text-align: left;
  color: #AFB6C1;
  margin: 0;
}
select {
  padding: 10px;
  font-family: TT Norms Medium;
  font-size: 14px;
  line-height: 20px;
  color: #D2D8DE;
  border: none;
  background-color: #F3F5F6;
  border-radius: 3px;
}
input{
  margin: 0;
}
select option {
  font-family: TT Norms Medium;
  font-size: 14px;
  line-height: 20px;
  color: #535C69;
}
select#service {
  width: 100%;
  padding: 10px;
  font-family: TT Norms Medium;
  font-size: 14px;
  line-height: 20px;
  color: #D2D8DE;
  border: none;
  background-color: #F3F5F6;
}
label{
  margin: 0;
}
.color_text{
  font-family: TT Norms Medium;
  font-size: 12px;
  line-height: 14px;
  letter-spacing: 0em;
  text-align: left;
  color: #52565F;
}
.color_container{
  display: flex;
  gap: 5px;
}
.color{
  width: 24px;
  height: 24px;
  border-radius: 3px;
  cursor: pointer;
}
.bottom_container{
  display: flex;
  gap: 10px;
  width: 50%;
}
.bottom{
  display: flex;
  justify-content: space-between;
}
.save{
  background: #EFEFFF;
  color: #6266EA;
  width: 100%;
}
.back{
  color: #535C69;
  background: #FFFFFF;
  border: 1px solid #DDE1E5;
  width: 100%;
}
.save:hover{
  color: #FFFFFF;
  background: #6266EA;
}
.delete{
  color: #F97F7F;
  background: #F97F7F33;
}
.delete:hover{
  background: #F97F7F;
  color: #FFFFFF;
}
.small-text {
  color:#D2D8DE;
  font-family: "TT Norms Medium";
  font-size: 14px;
  font-style: normal;
  font-weight: 500;
  line-height: normal;
  text-align: left;
  margin: 0;
}
.small-text .remaining-characters {
  color: #6266EA;
}
.modal{
  width: 36vh;
  height: auto;
  position: absolute;
  padding: 40px;
  border-radius: 10px;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  background: white;
  z-index: 99 ;
}
.delete_edit{
  color: #F97F7F;
  background-color: rgba(249, 127, 127, 0.2);
}
.delete:hover{
  background: #F97F7F;
  color: #FFFFFF;
}
.exit{
  color: #535C69;
  border: 1px solid #DDE1E5;
  background: #FFFFFF;  
  transition: background-color 0.3s, border-color 0.3s, color 0.3s;
}
.exit:hover{
  border: 1px solid #AFB6C1;
  background: #F5F5F5;
}
.btn_container{
  margin-top: 30px;
  display: flex;
  gap: 10px;
}
.text-header{
  font-family: TT Norms Medium;
  font-size: 14px;
  line-height: 14px;
  letter-spacing: 0em;
  color: #535C69;
  margin: 0;
  text-align: left;
}
.modal-subtext{
  font-family: TT Norms Medium;
  font-size: 14px;
  font-weight: 500;
  line-height: 20px;
  letter-spacing: 0em;
  text-align: left;
  color: #AFB6C1;
  margin: 0;
  margin-top: 10px;
}
.modal_span{
  color: #7D838C;
}
.overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.6); /* Задний фон с прозрачностью 60% */
  z-index: 98;
}
</style>