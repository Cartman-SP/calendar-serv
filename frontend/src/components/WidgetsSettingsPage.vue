<template>
  <div class="main">
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
              <div class="app-group">
                <p>Instagram</p>
                <InputSwitchComponent v-model="switches.instagram" style="margin-top: 5px;"/>
              </div>
            </div>
            <div class="apps">
              <div class="app-group">
                <p>WhatsApp</p>
                <InputSwitchComponent v-model="switches.whatsapp" style="margin-top: 5px;"/>
              </div>
              <div class="app-group">
                <p>Вконтакте</p>
                <InputSwitchComponent v-model="switches.vkontakte" style="margin-top: 5px;"/>
              </div>
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
              <select id="widget-time">
                <option value="" disabled selected style="display:none;">Время</option>
                <option value="30m">30 Минут</option>
                <option value="1h">1 Час</option>
              </select>
            </div>
            <div class="footer-apps">
              <p class="header">Ограничение на отмену</p>
              <p class="subheader">Время, за которое клиент не<br> сможет отменять записи</p>
              <select id="widget-time" style="width: auto">
                <option value="" disabled selected style="display:none;">Время</option>
                <option value="30m">30 Минут</option>
                <option value="1h">1 Час</option>
              </select>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
  
  <script>
  export default {
    data() {
      return {
        switches: {
          telegram: false,
          instagram: false,
          whatsapp: false,
          vkontakte: false,
          feedback: false,
          company: false,
          employee: false,
          cancellation: false,
        }
      };
    },
  }
  </script>
  
  <style scoped>
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
    width: 50%;
  }
  .app-group{
    display: flex;
    justify-content: start;
    align-items: center;
  }
  .navigation {
    display: flex;
    background-color:#FAFAFA;
  }
  
  .settings {
    text-align: center;
    width: 615px;
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
    width: 80px;
    font-family: TT Norms;
    font-size: 14px;
    font-weight: bold;
    line-height: 17px;
    color:#535C69;
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
    padding: 10px;
    font-family: TT Norms;
    font-size: 16px;
    line-height: 20px;
    color: #D2D8DE;
    border: none;
    background-color: #F3F5F6;
    border-radius: 3px;
    width: 100%;
  }
  
  select option {
    font-family: TT Norms;
    font-size: 16px;
    font-weight: bold;
    line-height: 20px;
    color: #535C69;
  }
  .apps-container{
    display: flex;
    justify-content: space-between;
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
  </style>