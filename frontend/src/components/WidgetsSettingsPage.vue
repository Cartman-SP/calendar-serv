<template>
  <div class="main">
    <div class="transition">
      <router-link to="/lk/widgets" class="employesss-link">Виджеты</router-link>
      <div class="arrow-container">
        <img src="../../static/img/arrow-right.png" alt="Стрелка вправо" class="arrow-icon">
      </div>
      <p class="creation_text">Создание виджета</p>
    </div>
    <div class="tab" ref="tabs">
      <div :class="{'tab-link': true, 'active-tab': selectedTab === 'general'}" @click="selectTab('general')">Общие настройки</div>
      <div :class="{'tab-link': true, 'active-tab': selectedTab === 'design'}" @click="selectTab('design')">Дизайн</div>
      <div :class="{'tab-link': true, 'active-tab': selectedTab === 'notifications'}" @click="selectTab('notifications')">Уведомления</div>
      <div :class="{'tab-link': true, 'active-tab': selectedTab === 'telegram'}" @click="selectTab('telegram')">Telegram-бот</div>
      <div :class="{'tab-link': true, 'active-tab': selectedTab === 'integrations'}" @click="selectTab('integrations')">Интеграции и оплаты</div>
      <div :class="{'tab-link': true, 'active-tab': selectedTab === 'discounts'}" @click="selectTab('discounts')">Скидки и промокоды</div>
      <div :class="{'tab-link': true, 'active-tab': selectedTab === 'custom'}" @click="selectTab('custom')">Свой код</div>
    </div>
    <div class="card">
      <div v-if="selectedTab === 'general'">
        <div class="navigation">
          <div class="settings">
            <div class="forms">
              <div class="name-container">
                <div class="input-content">
                  <label for="widgetName">Название виджета</label>
                  <input type="text" id="widgetName" placeholder="Мой виджет">
                </div>
    
                <div class="input-content">
                  <label for="widgetLanguage">Язык виджета</label>
                  <select id="widgetLanguage">
                    <option value="" disabled selected style="display:none;">Выберите язык</option>
                    <option value="russian">Русский</option>
                    <option value="belarusian">Белорусский</option>
                  </select>
                </div>
              </div>
              <div class="apps-container">
                <div class="apps">
                  <div class="app-group">
                    <p>Telegram</p>
                    <InputSwitchComponent v-model="switches.telegram" style="margin-top: 5px;"/>
                  </div>
                  <input type="text">
                  <div class="app-group">
                    <p>Instagram</p>
                    <InputSwitchComponent v-model="switches.instagram" style="margin-top: 5px;"/>
                  </div>
                  <input type="text" class="">
                </div>
                <div class="apps">
                  <div class="app-group">
                    <p>WhatsApp</p>
                    <InputSwitchComponent v-model="switches.whatsapp" style="margin-top: 5px;"/>
                  </div>
                  <input type="text">
                  <div class="app-group">
                    <p>Вконтакте</p>
                    <InputSwitchComponent v-model="switches.vkontakte" style="margin-top: 5px;"/>
                  </div>
                  <input type="text">
                </div>
              </div>
              <label for="widgetbranch">Филиалы</label>
                  <select id="widgetbranch" style="width: 100%;">
                    <option value="" disabled selected style="display:none;">Выберите филиалы</option>
                  </select>
              <div class="footer">
                <div class="footer-apps">
                  <p class="header">Отзывы</p>
                  <p class="subheader">Клиенты смогут увидеть рейтинг<br>и отзывы о вашем филиале</p>
                  <InputSwitchComponent v-model="switches.feedback" />
                </div>
                <div class="footer-apps">
                  <p class="header">О компании</p>
                  <p class="subheader">Клиенты смогут увидеть рейтинг<br>и отзывы о вашем филиале</p>
                  <InputSwitchComponent v-model="switches.company" />
                </div>
                <div class="footer-apps">
                  <p class="header">Любой сотрудник</p>
                  <p class="subheader">Клиенты смогут записываться,<br> пропустив выбор сотрудника</p>
                  <InputSwitchComponent v-model="switches.employee" />
                </div>
                <div class="footer-apps">
                  <p class="header">Отмена записи</p>
                  <p class="subheader">Позволяет клиентам в режиме<br> онлайн отменять записи</p>
                  <InputSwitchComponent v-model="switches.cancellation" />
                </div>
                <div class="footer-apps">
                  <p class="header">Интервал записи</p>
                  <p class="subheader">Задержка времени между<br> сеансами</p>
                  <select id="widget-time" style="width: 70%">
                    <option value="" disabled selected style="display:none;">Время</option>
                    <option value="30m">30 Минут</option>
                    <option value="1h">1 Час</option>
                  </select>
                </div>
                <div class="footer-apps">
                  <p class="header">Ограничение на отмену</p>
                  <p class="subheader">Время, за которое клиент не<br> сможет отменять записи</p>
                  <select id="widget-time" style="width: 70%">
                    <option value="" disabled selected style="display:none;">Время</option>
                    <option value="30m">30 Минут</option>
                    <option value="1h">1 Час</option>
                  </select>
                </div>
              </div>
              <div class="button-container">
                <button @click="save" class="save-button">Сохранить</button>
                <button @click="cancel" class="cancel-button">Отмена</button>
              </div>
            </div>
          </div>
          <WidgetApp></WidgetApp>
        </div>
      </div>
      <div v-if="selectedTab === 'design'">
        <div class="navigation">
          <div class="settings">
            <p class="header">Обложка виджета</p>
            <p class="descr">Выберите фотографию для обложки из ранее загруженных или добавьте новую</p>
            <div class="plus_container">
              <div class="img_plus" @click="uploadImage">
                <input type="file" style="display: none;" @change="handleImageUpload">
                <img src="" alt="">
              </div>
              <div class="img_plus" @click="uploadImage">
                <input type="file" style="display: none;" @change="handleImageUpload">
                <img src="" alt="">
              </div>
              <div class="img_plus" @click="uploadImage">
                <input type="file" style="display: none;" @change="handleImageUpload">
                <img src="" alt="">
              </div>
              <div class="img_plus" @click="uploadImage">
                <input type="file" style="display: none;" @change="handleImageUpload">
                <img src="" alt="">
              </div>
              <div class="img_plus" @click="uploadImage">
                <input type="file" style="display: none;" @change="handleImageUpload">
                <img src="" alt="">
              </div>
            </div>
            <div class="color_container">
              <div class="color">
                <p class="header">Цветовой схема</p>
                <div class="switch_container">
                  <p class="light">Светлая</p>
                  <InputSwitchComponent v-model="switches.theme" style="margin-top: 5px;"/>
                  <p class="dark">Тёмная</p>
                </div>
              </div>
              <div class="color">
                <p class="header">Основной</p>
                <div class="rgb" v-click-outside="resetSelection">
                  <p class="rgb_color">govno</p>
                  <div class="rgb_choise" @click="toggleSelection"></div>
                  <PalitraPage v-if="isCircleShown" class="show"></PalitraPage>
                </div>
              </div>
              <div class="color">
                <p class="header">Фон виджета</p>
                <div class="rgb">
                  <p class="rgb_color">govno</p>
                  <div class="rgb_choise" @click="toggleSelection"></div>
                  <PalitraPage v-if="isCircleShown" class="show"></PalitraPage>
                </div>
              </div>
              <div class="color">
                <p class="header">Фон плашка</p>
                <div class="rgb">
                  <p class="rgb_color">govno</p>
                  <div class="rgb_choise" @click="toggleSelection"></div>
                  <PalitraPage v-if="isCircleShown" class="show"></PalitraPage>
                </div>
              </div>
              <div class="color">
                <p class="header">Цвет текста</p>
                <div class="rgb">
                  <p class="rgb_color">govno</p>
                  <div class="rgb_choise" @click="toggleSelection"></div>
                  <PalitraPage v-if="isCircleShown" class="show"></PalitraPage>
                </div>
              </div>
            </div>
            <p class="header" style="margin-bottom:10px">Выберите дизайн виджета</p>
            <div class="wrapper">
              <div class="window_container">
                <div class="window">
                  <div class="square"></div>
                  <div class="stripe"></div>
                  <div class="stripe"></div>
                  <div class="stripe"></div>
                  <div class="rectangle"></div>
                </div>
                <div class="choice" @click="activateChoice" data-type="site">
                  <div class="circle_bottom">
                    <div class="second_circle"></div>
                  </div>
                  <p class="">Виджет в виде сайта</p>
                </div>
              </div>
              <div class="window_container">
                <div class="window">
                  <div class="stripe"></div>
                  <div class="stripe" style="width:80%"></div>
                  <div class="stripe" style="width:60%"></div>
                  <div class="rectangle"></div>
                </div>
                <div class="choice" @click="activateChoice" data-type="embedded">
                  <div class="circle_bottom">
                    <div class="second_circle"></div>
                  </div>
                  <p>Встроенный виджет<br>для вашего сайта</p>
                </div>
              </div>
              <div class="window_container">
                <div class="window">
                  <div class="lane_container">
                    <div class="lane" style="width:32%"></div>
                    <div class="lane" style="width:62%"></div>
                  </div>
                  <div class="stripe" style="width:80%"></div>
                  <div class="stripe" style="width:60%"></div>
                  <div class="stripe" style="width:40%"></div>
                  <div class="lane_container">
                    <div class="lane" style="width:55%"></div>
                    <div class="circle"></div>
                  </div>
                </div>
                <div class="choice" @click="activateChoice" data-type="floating">
                  <div class="circle_bottom">
                    <div class="second_circle"></div>
                  </div>
                  <p>Плавающая кнопка<br> на вашем сайте</p>
                </div>
              </div>
            </div>
            <p>Прямая ссылка на виджет</p>
            <input type="text">
            <div class="button-container">
              <button @click="save" class="save-button">Сохранить</button>
              <button @click="cancel" class="cancel-button">Отмена</button>
            </div>
          </div>
          <WidgetApp></WidgetApp>
        </div>
      </div>
      <div v-if="selectedTab === 'notifications'">
        <!-- Содержимое для уведомлений -->
      </div>
      <div v-if="selectedTab === 'telegram'">
        <!-- Содержимое для Telegram-бота -->
      </div>
      <div v-if="selectedTab === 'integrations'">
        <!-- Содержимое для интеграций и оплат -->
      </div>
      <div v-if="selectedTab === 'discounts'">
        <!-- Содержимое для скидок и промокодов -->
      </div>
      <div v-if="selectedTab === 'custom'">
        <!-- Содержимое для своего кода -->
      </div>
    </div>
  </div>
</template>
  
<script>
import WidgetApp from './WidgetApp.vue';
import PalitraPage from './PalitraPage.vue';

export default {
  components: { WidgetApp , PalitraPage} ,
  data() {
    return {
      selectedTab: 'general',
      switches: {
        telegram: false,
        instagram: false,
        whatsapp: false,
        vkontakte: false,
        feedback: false,
        company: false,
        employee: false,
        cancellation: false,
        theme: false,
      },
      selectedChoice: null, 
      isCircleShown: false, // Added property to track the display of the circle
    };
  },
  mounted() {
    // После монтирования компонента выбираем первую вкладку по умолчанию
    this.$refs.tabs.querySelectorAll('.tab-link')[0].click();
  },
  methods: {
    uploadImage(event) {
      // Find the associated file input element and trigger a click event
      const fileInput = event.target.querySelector('input[type="file"]');
      if (fileInput) {
        fileInput.click();
      }
    },
    handleImageUpload(event) {
      const file = event.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = (e) => {
          // Update the src of img_plus with the uploaded image
          event.target.closest('.img_plus').querySelector('img').src = e.target.result;
        };
        reader.readAsDataURL(file);
      }
    },
    toggleSelection() {
    // Toggle between showing the button and the circle
    this.isCircleShown = !this.isCircleShown;
    },
    resetSelection() {
      // Reset to the original state (hide the circle)
      this.isCircleShown = false;
    },
    selectTab(tab) {
      this.selectedTab = tab; // Функция для изменения выбранной вкладки
    },
    activateChoice(event) {
      const choice = event.currentTarget;
      const choiceType = choice.getAttribute('data-type');

      if (this.selectedChoice === choiceType) {
        this.selectedChoice = null;
        choice.querySelector('.second_circle').style.display = 'none';
        choice.querySelector('.circle_bottom').style.borderColor = '#C6CBD2';
      } else {
        this.selectedChoice = choiceType;
        document.querySelectorAll('.choice').forEach(choice => {
          choice.classList.remove('active');
          choice.querySelector('.second_circle').style.display = 'none';
          choice.querySelector('.circle_bottom').style.borderColor = '#C6CBD2';
        });
        choice.classList.add('active');
        choice.querySelector('.second_circle').style.display = 'inline-block';
        choice.querySelector('.circle_bottom').style.borderColor = '#6266EA';
      }
    },
  },
};
</script>
  
  <style scoped>
  .descr{
    font-family: TT Norms;
    font-size: 12px;
    font-weight: 500;
    line-height: 14px;
    letter-spacing: 0em;
    text-align: left;
    color: #AFB6C1;
    width: 100%;
    margin: 0 0 10px 0;
  }
  .header{
    margin: 20px 0 5px 0;
  }
  .subheader{
    margin-top: 0;
  }
  .header, .subheader{
    width: 100%;
  }
  .name-container{
    display: grid;
    grid-template-columns: 5fr 4fr;
    grid-column-gap: 20px;
    grid-row-gap: 0px; 
  }
  .apps{
    width: 100%;
  }
  .app-group{
    display: flex;
    justify-content: start;
    align-items: center;
    gap: 10px;
  }
  .navigation {
    display: flex;
    background-color:#FAFAFA;
    gap: 40px;
  }
  
  .settings {
    text-align: center;
    width: 55%;
    height: auto;
    background-color: #FFFFFF;
    padding: 20px;
    border-radius: 5px;
  }
  
  label {
    margin-right: 10px;
    margin-bottom: 10px;
    font-family: TT Norms;
    font-size: 13px;
    font-weight: bold;
    line-height: 15px;
    letter-spacing: 0em;
  }
  
  input {
    margin-bottom: 0;
    margin-right: 10px;
  }
  
  p{
    text-align: left;
    font-family: TT Norms;
    font-size: 14px;
    font-weight: bold;
    line-height: 17px;
    color:#535C69;
    margin: 10px 0;
  }

  input::placeholder {
    font-family: "TT Norms";
    font-size: 14px;
    font-weight: 500;
    line-height: 17px;
    letter-spacing: 0em;
    color: #D2D8DE;
  }
  
  select {
    width: 100%;
    padding: 8px 10px;
    font-family: TT Norms;
    font-size: 14px;
    line-height: 20px;
    color: #D2D8DE;
    border: none;
    background-color: #F3F5F6;
    margin-bottom: 10px;
    border-radius: 3px;
    height: 36px;
  }
  
  select option {
    font-family: TT Norms;
    font-size: 14px;
    font-weight: bold;
    line-height: 20px;
    color: #535C69;
  }
  .apps-container{
    display: grid;
    grid-template-columns: 5fr 4fr;
    grid-column-gap: 20px;
    grid-row-gap: 0px;
    margin-bottom: 10px;
  }
  .subheader{
    font-family: TT Norms;
    font-size: 10px;
    font-weight: 500;
    line-height: 12px;
    letter-spacing: 0em;
    text-align: left;
    color: #AFB6C1;
  }
  .footer{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-template-rows: repeat(2, 1fr);
    grid-column-gap: 20px;
    grid-row-gap: 20px; 
  }
  .footer-apps{
    display: flex;
    flex-direction: column;
  }
  .transition {
    display: flex;
    flex-direction: row;
    gap: 10px;
    margin-bottom: 20px;
  }
  
  .employesss-link {
    font-family: TT Norms;
    font-size: 20px;
    font-weight: bold;
    line-height: 24px;
    text-align: left;
    text-decoration: none;
    color: #AFB6C1;
  }
  
  .creation_text {
    color: #535C69;
    font-family: TT Norms;
    font-size: 20px;
    font-weight: bold;
    line-height: 24px;
    letter-spacing: 0em;
    text-align: left;
    margin: 0;
    width: 100%;
  }
  
  .arrow-container {
    display: flex;
    align-items: center;
  }
  
  .arrow-icon {
    height: 50%;
  }
  .plus_container{
    display: flex;
    gap: 10px;
  }
  .img_plus {
    width: 80px;
    height: 80px;
    border-radius: 5px;
    border: 1px solid #D2D8DE;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    background: url(../../static/img/plus.svg) center center/cover no-repeat;
    background-size: 25%;
  }
  
  .img_plus img {
    max-width: 80px;
    max-height: 80px;
  }
  .color_container{
    display: flex;
    gap: 10px;
  }
  .color{
    width: 100%;
    margin-right: 20px;
  }
  .rgb{
    width: 65%;
    height: auto;
    border-radius: 3px;
    padding: 5px 10px;
    border: 1px solid #D2D8DE;
    display: flex;
    gap: 10px;
    align-items: center;
    justify-content: center;
  }
  .rgb_color{
    margin: 0;
  }
  .rgb_choise{
    width: 12px;
    height: 12px;
    border: 1px solid #D2D8DE;
    border-radius: 25px;
    margin: 0;
  }
  .switch_container{
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .light{
    font-family: TT Norms;
    font-size: 12px;
    font-weight: 500;
    line-height: 10px;
    letter-spacing: 0em;
    text-align: left;
    color: #535C69;
    margin: 0;
  }
  .dark{
    font-family: TT Norms;
    font-size: 12px;
    font-weight: 500;
    line-height: 10px;
    letter-spacing: 0em;
    text-align: left;
    color: #AFB6C1;    
    margin: 0;
  }
  .window{
    width: 10vw;
    height: 120px;
    border-radius: 2px;
    padding: 15px;
    background: #F6F6F6;
    display: flex;
    flex-direction: column;
    gap: 5px;
  }
  .stripe {
    background: linear-gradient(90deg, #EBEBEB 0%, #DAE2EE 100%);
    border-radius: 2px;
    width: 100%;
    height: 20px;
  }
  .square{
    width: 20px;
    height: 45px;
    background: linear-gradient(90deg, #EBEBEB 0%, #DAE2EE 100%);
    border-radius: 2px;
  }
  .rectangle{
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, #9497FF 0%, #8B8FFF 100%);
    border-radius: 2px;
  }
  .wrapper{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-template-rows: 1fr;
    grid-column-gap: 20px;
  }
  .button-container {
    display: flex;
    gap: 10px;
    justify-content: flex-end;
    margin-top: 20px;
  }
  .save-button {
    background-color: #EFEFFF;
    color: #6266EA;
    transition: background-color 0.3s, color 0.3s;
  }
  
  .save-button:hover {
    background-color: #464AD9;
    color: #EFEFFF;
  }
  .cancel-button {
    background-color: #FFFFFF;
    color: #535C69;
    border-radius: 3px;
    border: 1px solid #DDE1E5
  }
  .lane_container{
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
  }
  .lane{
    height: 15px;
    background: linear-gradient(90deg, #EBEBEB 0%, #DAE2EE 100%);
    border-radius: 2px;
  }
  .circle{
    width: 30px;
    height: 30px;
    background: linear-gradient(90deg, #9497FF 0%, #8B8FFF 100%);
    border-radius: 100px;
  }
  .card{
    background: #FAFAFA;
    padding: 10px;
    margin: 10px 0;
  }
  .tab{
    position: relative;
    border-bottom: 1px solid rgba(50, 56, 74, 0.1); 
    width: 68%;
    display: flex;
    gap: 15px;
    margin-top: 30px;
    padding: 0;
  }
  .tab-link {
    position: relative;
    font-family: TT Norms;
    font-size: 14px;
    font-weight: 500;
    line-height: 17px;
    letter-spacing: 0em;
    text-align: left;
    color: #AFB6C1;
    cursor: pointer;
    padding-bottom: 10px;
  }
  .tab-link:hover {
    color: #6266EA;
  }
  .tab-link::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 2px;
    background-color: transparent;
    transition: background-color 0.3s;
  }
  
  .tab-link:hover::after {
    background-color: #6266EA;
  }
  .window_container{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
  .active-tab {
    color: #6266EA;
  }
  .active-tab::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 2px;
    background-color: transparent;
    transition: background-color 0.3s;
    background:#6266EA;
  }
  .choice{
    display: flex;
    gap: 5px;
    align-items: center;
    cursor: pointer;
    height: 55px;
  }
  .circle_bottom{
    display: flex;
    justify-content: center;
    align-items: center;
    width: 18px;
    height: 18px;
    border: 1px solid #C6CBD2;
    background: #F3F5F6;
    border-radius: 15px;
    cursor: pointer;
  }
  .second_circle{
    background: #6266EA;
    width: 10px;
    height: 10px;
    border-radius: 25px;
    display: none;
  }
  .choice.active .circle_bottom {
    border-color: #6266EA; /* добавили изменение цвета границы для активного choice */
  }
  </style>