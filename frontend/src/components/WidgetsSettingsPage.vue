<template>
  <div class="main">
    <div class="transition">
      <router-link to="/dashboard/widgets" class="employesss-link">Виджеты</router-link>
      <div class="arrow-container">
        <img src="../../static/img/arrow-right.png" alt="Стрелка вправо" class="arrow-icon">
      </div>
      <p class="creation_text">Редактирование виджета</p>

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
        <div class="navigation" v-if="selectedTab === 'general'">
          <div class="settings">
            <div class="forms">
              <div class="name-container">
                <div class="input-content">
                  <label for="widgetName">Название виджета</label>
                  <input type="text" id="widgetName" placeholder="Мой виджет" v-model="widgetName">
                </div>
    
                <div class="input-content">
                  <label for="widgetLanguage">Язык виджета</label>
                  <SelectPage
                  :options="['Русский', 'Белорусский']"
                  class="select" @input="option => selectedLanguage = option"
                  :placeholderdata="'Выберите язык'"
                  />
                </div>
              </div>
              <div class="apps-container">
                <div class="apps">
                  <div class="app-group">
                    <p>Telegram</p>
                    <InputSwitchComponent v-model="switches.telegram" style="margin-top: 5px;"/>
                  </div>
                  <input v-if="switches.telegram" type="text" v-model="widgetLinkTelegram">
                  <div class="app-group">
                    <p>Instagram</p>
                    <InputSwitchComponent v-model="switches.instagram" style="margin-top: 5px;"/>
                  </div>
                  <input v-if="switches.instagram" type="text" v-model="widgetLinkInstagram" class="">
                </div>
                <div class="apps">
                  <div class="app-group">
                    <p>WhatsApp</p>
                    <InputSwitchComponent v-model="switches.whatsapp" style="margin-top: 5px;"/>
                  </div>
                  <input v-if="switches.whatsapp" type="text" v-model="widgetLinkWhatsApp">
                  <div class="app-group">
                    <p>Вконтакте</p>
                    <InputSwitchComponent v-model="switches.vkontakte" style="margin-top: 5px;"/>
                  </div>
                  <input v-if="switches.vkontakte" type="text" v-model="widgetLinkVk">
                </div>
              </div>
              <label for="widgetbranch">Филиалы</label>
              <SelectPage
                  :options="[{
                    name: 'qwdqwd',
                    id: '23'
                  },{
                    name: 'ddfbbbbbb',
                    id: '3777'
                  }]"
                  class="select" @input="handleSelectInput"
                  :placeholderdata="'Выберите филиалы'"
                  />
              <div class="chips-block">
                <div class="chip" v-for="chip in filteredChips" :key="chip.id">
                  <svg @click="deleteChip(chip)" width="8" height="8" viewBox="0 0 6 6" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M2.29294 3.00003L0.146484 5.14648L0.853591 5.85359L3.00004 3.70714L5.1465 5.85359L5.85361 5.14648L3.70715 3.00003L5.85359 0.853591L5.14648 0.146484L3.00004 2.29292L0.853605 0.146484L0.146499 0.853591L2.29294 3.00003Z" fill="white"/>
                  </svg>
                  <p>{{ chip.name }}</p>
                </div>
              </div>
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
                  <SelectPage
                  :options="['15 минут', '30 минут', '1 час', '2 часа','3 часа','4 часа']"
                  :placeholderdata="'Выберите время'"
                  class="select" @input="option => selectedInterval = option"
                  style="width: 90%;"
                  />
                </div>
                <div class="footer-apps">
                  <p class="header">Ограничение на отмену</p>
                  <p class="subheader">Время, за которое клиент не<br> сможет отменять записи</p>
                  <SelectPage
                  :options="['30 минут', 'за 1 час', 'за 2 часа','за 3 часа','за 4 часа','за 5 часов']"
                  class="select" @input="option => selectedOgranichenie = option"
                  :placeholderdata="'Выберите время'"
                  style="width: 90%;"
                  />
                </div>
              </div>
              <div class="button-container">
                <button @click="save" class="save-button">Сохранить</button>
                <button @click="cancel" class="cancel-button">Отмена</button>
              </div>
            </div>
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
                  <InputSwitchComponent v-model="switches.theme" @change="themechange" style="margin-top: 5px;"/>
                  <p class="dark">Тёмная</p>
                </div>
              </div>
              <div class="color">
                <p class="header">Основной</p>
                <div class="rgb" @click="toggleSelection(1)">
                  <p class="rgb_color">{{ widget.Main }}</p>
                  <div class="rgb_choise" :style="{ backgroundColor: widget.Main }"></div>
                  <PalitraPage v-if="isCircleShown1" class="show" @updateColor="color => handleColorUpdate(color, 1)"></PalitraPage>
                </div>
              </div>
              <div class="color">
                <p class="header">Фон виджета</p>
                <div class="rgb" @click="toggleSelection(2)">
                  <p class="rgb_color">{{ widget.Back }}</p>
                  <div class="rgb_choise" :style="{ backgroundColor: widget.Back }"></div>
                  <PalitraPage v-if="isCircleShown2" class="show" @updateColor="color => handleColorUpdate(color, 2)"></PalitraPage>
                </div>
              </div>
              <div class="color">
                <p class="header">Фон плашка</p>
                <div class="rgb" @click="toggleSelection(3)">
                  <p class="rgb_color">{{ widget.Plashka }}</p>
                  <div class="rgb_choise" :style="{ backgroundColor: widget.Plashka }"></div>
                  <PalitraPage v-if="isCircleShown3" class="show" @updateColor="color => handleColorUpdate(color, 3)"></PalitraPage>
                </div>
              </div>
              <div class="color">
                <p class="header">Цвет текста</p>
                <div class="rgb" @click="toggleSelection(4)">
                  <p class="rgb_color">{{ widget.Text }}</p>
                  <div class="rgb_choise" :style="{ backgroundColor: widget.Text }"></div>
                  <PalitraPage v-if="isCircleShown4" class="show" @updateColor="color => handleColorUpdate(color, 4)"></PalitraPage>
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
            <input type="text" v-model="widgetLink">
            <div class="button-container">
              <button @click="save" class="save-button">Сохранить</button>
              <button @click="cancel" class="cancel-button">Отмена</button>
            </div>
          </div>
        </div>
      </div>
      <div v-if="selectedTab === 'notifications'">
        <!-- Содержимое для уведомлений -->
      </div>
      <div class="telegram" v-if="selectedTab === 'telegram'">
        <div class="telegram_main">
          <div class="telegram_header">
            <div>
              <p class="telegram_label">Telegram-токен бота</p>
              <input v-model="telegramToken" style="width: 100%;" type="text" placeholder="123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11">
            </div>
            <button :class="{'telegram_button-active' : telegramToken, 'telegram_button-disabled' : !telegramToken}">Подключить</button>
          </div>
          <div class="telegram_description">
            <p class="telegram_label">Где взять Telegram-токен?</p>
            <ol>
              <li>Перейдите в чат с ботом <span style="color: #535C69; text-decoration: underline;">@BotFather</span> в Telegram</li>
              <li>Отправьте команду /newbot , чтобы создать нового бота</li>
              <li>Укажите name и username</li>
              <li>В ответ @BotFather пришлет токен вашего бота <br> в формате: 123456:ABC-DEF1234ghIkl-<br>zyx57W2v1u123ew11</li>
              <li>Укажите его в поле Telegram-токен бота</li>
            </ol>
          </div>
        </div>
        <div class="telegram_main">
          <section>
            <p class="telegram_label">Приветственное сообщение</p>
            <textarea placeholder="Введите текст для приветственного сообщения" class="custom_input" v-model="symbols3" name="helloMsg" rows="5"></textarea>
            <div class="tg-row">
              <p class="textarea_subtitle">Это сообщение увидят новые клиенты</p>
              <p class="symbols_counter">{{symbols3.length}}/200</p>
            </div>
          </section>
          <section>
            <p class="telegram_label">Название кнопки открытия бота</p>
            <textarea placeholder="Например: Записаться сейчас" class="custom_input" v-model="symbols4" name="btnName" rows="1"></textarea>
            <div class="tg-row">
              <p class="textarea_subtitle">Не длиннее указанного количества символов</p>
              <p class="symbols_counter">{{symbols4.length}}/25</p>
            </div>
          </section>
        </div>
        <img v-show="false" src="../../static/img/bot.svg" alt="">
      </div>
      <div v-if="selectedTab === 'integrations'" class="integrations">
        <div class="integrations_first">
          <div class="integrations_header">
            <button class="integrations_btn" @click="startCreatingPromoCode">
              <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M9.00006 11V17H11.0001V11H17V9H11.0001V3H9.00006V9H3V11H9.00006Z" fill="#D2D8DE"/>
              </svg>
              Добавить интеграцию
            </button>
            <input type="text" placeholder="Поиск" class="integrations_input">
          </div>
          <div class="integrations_nav">
            <div class="integrations_nav_container">
              <p class="integrations_nav_text">Статус</p>
              <p class="integrations_nav_text">ID</p>
              <p class="integrations_nav_text">Подключено</p>
              <p class="integrations_nav_text">Система</p>
              <p class="integrations_nav_text">Название</p>
              <p class="integrations_nav_text">Действия</p>
            </div>
            <div class="divider"></div>
          </div>
          <div class="integrations_new">
            <div class="integrations_new_container">
              <p class="integrations_new_header">Здесь вы можете подключить: CRM-систему, Email-рассылки, виджеты онлайн-оплаты, уведомления и т.д.</p>
              <p class="krest">&times;</p>
            </div>
            <div class="integrations_new_btn">
              <button @click="startCreatingPromoCode">Понятно</button>
              <button class="ponyatno">Подключить интеграцию</button>
            </div>
          </div>
          <div class="integrations_main">
            <p class="integrations_main_text">1254654</p>
            <p class="integrations_main_text">37066</p>
            <p class="integrations_main_text">27.12.2023 18:27</p>
            <p class="integrations_main_text">AmoCRM AmoCRM</p>
            <p class="integrations_main_text">Выгрузка в CRM </p>
            <div class="integrations_main_items_container">
              <div class="integrations_main_items">
                <svg id="edit" width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <rect width="16" height="16" fill="white"/>
                  <path fill-rule="evenodd" clip-rule="evenodd" d="M7.05788 0.400024C6.84974 0.400024 6.68102 0.56875 6.68102 0.776884V2.19817C6.09375 2.34332 5.53152 2.57563 5.01308 2.88734L4.01148 1.88314C3.94083 1.81232 3.84493 1.77249 3.7449 1.77242C3.64486 1.77236 3.54891 1.81207 3.47817 1.8828L1.8828 3.47817C1.81207 3.54891 1.77236 3.64486 1.77242 3.7449C1.77249 3.84493 1.81232 3.94083 1.88314 4.01148L2.88734 5.01308C2.57563 5.53152 2.34332 6.09375 2.19817 6.68102H0.776884C0.56875 6.68102 0.400024 6.84974 0.400024 7.05788V8.94217C0.400024 9.15031 0.56875 9.31903 0.776884 9.31903H2.19817C2.34332 9.90629 2.57563 10.4685 2.88734 10.987L1.88314 11.9886C1.81232 12.0592 1.77249 12.1551 1.77242 12.2552C1.77236 12.3552 1.81207 12.4511 1.8828 12.5219L3.47817 14.1172C3.54891 14.188 3.64486 14.2277 3.7449 14.2276C3.84493 14.2276 3.94083 14.1877 4.01148 14.1169L5.01308 13.1127C5.53152 13.4244 6.09375 13.6567 6.68102 13.8019V15.2232C6.68102 15.4313 6.84974 15.6 7.05788 15.6H8.94217C9.15031 15.6 9.31903 15.4313 9.31903 15.2232V13.8019C9.90629 13.6567 10.4685 13.4244 10.987 13.1127L11.9886 14.1169C12.0592 14.1877 12.1551 14.2276 12.2552 14.2276C12.3552 14.2277 12.4511 14.188 12.5219 14.1172L14.1172 12.5219C14.188 12.4511 14.2277 12.3552 14.2276 12.2552C14.2276 12.1551 14.1877 12.0592 14.1169 11.9886L13.1127 10.987C13.4244 10.4685 13.6567 9.90629 13.8019 9.31903H15.2232C15.4313 9.31903 15.6 9.15031 15.6 8.94217V7.05788C15.6 6.84974 15.4313 6.68102 15.2232 6.68102H13.8019C13.6567 6.09375 13.4244 5.53152 13.1127 5.01308L14.1169 4.01148C14.1877 3.94083 14.2276 3.84493 14.2276 3.7449C14.2277 3.64486 14.188 3.54891 14.1172 3.47817L12.5219 1.8828C12.4511 1.81207 12.3552 1.77236 12.2552 1.77242C12.1551 1.77249 12.0592 1.81232 11.9886 1.88314L10.987 2.88734C10.4685 2.57563 9.90629 2.34332 9.31903 2.19817V0.776884C9.31903 0.56875 9.15031 0.400024 8.94217 0.400024H7.05788ZM5.36201 8.00002C5.36201 6.54309 6.54309 5.36201 8.00002 5.36201C9.45696 5.36201 10.638 6.54309 10.638 8.00002C10.638 9.45696 9.45696 10.638 8.00002 10.638C6.54309 10.638 5.36201 9.45696 5.36201 8.00002Z" fill="#D2D8DE"/>
                </svg>
                <svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <g clip-path="url(#clip0_5101_42260)">
                    <path d="M7.58329 11.6667C8.35656 11.6658 9.09789 11.3582 9.64467 10.8114C10.1914 10.2646 10.499 9.52327 10.5 8.75001V3.64176C10.5009 3.33514 10.4409 3.03138 10.3235 2.7481C10.2062 2.46483 10.0338 2.20766 9.81629 1.99151L8.50846 0.683677C8.29231 0.466195 8.03514 0.293778 7.75187 0.176422C7.46859 0.0590653 7.16483 -0.000897138 6.85821 1.01439e-05H4.08329C3.31003 0.000936394 2.5687 0.308525 2.02192 0.855305C1.47514 1.40209 1.16755 2.14341 1.16663 2.91668V8.75001C1.16755 9.52327 1.47514 10.2646 2.02192 10.8114C2.5687 11.3582 3.31003 11.6658 4.08329 11.6667H7.58329ZM2.33329 8.75001V2.91668C2.33329 2.45255 2.51767 2.00743 2.84586 1.67924C3.17404 1.35105 3.61916 1.16668 4.08329 1.16668C4.08329 1.16668 6.95271 1.17484 6.99996 1.18068V2.33334C6.99996 2.64276 7.12288 2.93951 7.34167 3.1583C7.56046 3.37709 7.85721 3.50001 8.16663 3.50001H9.31929C9.32513 3.54726 9.33329 8.75001 9.33329 8.75001C9.33329 9.21414 9.14892 9.65926 8.82073 9.98745C8.49254 10.3156 8.04742 10.5 7.58329 10.5H4.08329C3.61916 10.5 3.17404 10.3156 2.84586 9.98745C2.51767 9.65926 2.33329 9.21414 2.33329 8.75001ZM12.8333 4.66668V11.0833C12.8324 11.8566 12.5248 12.5979 11.978 13.1447C11.4312 13.6915 10.6899 13.9991 9.91663 14H4.66663C4.51192 14 4.36354 13.9386 4.25415 13.8292C4.14475 13.7198 4.08329 13.5714 4.08329 13.4167C4.08329 13.262 4.14475 13.1136 4.25415 13.0042C4.36354 12.8948 4.51192 12.8333 4.66663 12.8333H9.91663C10.3808 12.8333 10.8259 12.649 11.1541 12.3208C11.4823 11.9926 11.6666 11.5475 11.6666 11.0833V4.66668C11.6666 4.51197 11.7281 4.36359 11.8375 4.2542C11.9469 4.1448 12.0953 4.08334 12.25 4.08334C12.4047 4.08334 12.553 4.1448 12.6624 4.2542C12.7718 4.36359 12.8333 4.51197 12.8333 4.66668Z" fill="#AFB6C1"/>
                  </g>
                  <defs>
                    <clipPath id="clip0_5101_42260">
                      <rect width="14" height="14" fill="white"/>
                    </clipPath>
                  </defs>
                </svg>
                <svg id="delete" width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path fill-rule="evenodd" clip-rule="evenodd" d="M3.36363 1.77778C3.36363 1.34822 3.72994 1 4.18181 1H11.8182C12.2701 1 12.6364 1.34822 12.6364 1.77778C12.6364 2.20733 12.2701 2.55556 11.8182 2.55556H4.18181C3.72994 2.55556 3.36363 2.20733 3.36363 1.77778ZM2.81818 5.66667H2V4.11111H14V5.66667H13.1818V12.1481C13.1818 13.7232 11.8387 15 10.1818 15H5.81818C4.16132 15 2.81818 13.7232 2.81818 12.1481V5.66667ZM11.5455 5.66667H4.45455V12.1481C4.45455 12.8641 5.06508 13.4444 5.81818 13.4444H10.1818C10.9349 13.4444 11.5455 12.8641 11.5455 12.1481V5.66667Z" fill="#D2D8DE"/>
                </svg>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div v-if="selectedTab === 'discounts' && !isCreatingPromoCode" class="discounts">
        <div class="discounts_first">
          <div class="discounts_header">
            <button class="discounts_btn" @click="startCreatingPromoCode">
              <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M9.00006 11V17H11.0001V11H17V9H11.0001V3H9.00006V9H3V11H9.00006Z" fill="#D2D8DE"/>
              </svg>
              Создать промокод
            </button>
            <input type="text" placeholder="Найти промокод" class="discounts_input">
          </div>
          <div class="discounts_nav">
            <div class="discounts_nav_container">
              <p class="discounts_nav_text">ID</p>
              <p class="discounts_nav_text">Название</p>
              <p class="discounts_nav_text">Дата начала</p>
              <p class="discounts_nav_text">Дата окончания</p>
              <p class="discounts_nav_text">Количество кодов</p>
            </div>
            <div class="divider"></div>
          </div>
          <div class="discounts_new">
            <div class="discounts_new_container">
              <p class="discounts_new_header">Сейчас у вас нет созданных промо-акций для ваших клиентов, однако, вы легко это исправить :)</p>
              <p class="krest">&times;</p>
            </div>
            <div class="discounts_new_btn">
              <button @click="startCreatingPromoCode">Создать промокод</button>
              <button class="ponyatno">Ясно, понятно</button>
            </div>
          </div>
          <div class="discounts_main">
            <p class="discounts_main_text">1254654</p>
            <p class="discounts_main_text">Скидка 50% клиен...</p>
            <p class="discounts_main_text">28.04.2024</p>
            <p class="discounts_main_text">1.05.2024</p>
            <div class="discounts_main_items_container">
              <p class="discounts_main_text">50</p>
              <div class="discounts_main_items">
                <svg id="edit" width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <rect width="16" height="16" fill="white"/>
                  <path fill-rule="evenodd" clip-rule="evenodd" d="M7.05788 0.400024C6.84974 0.400024 6.68102 0.56875 6.68102 0.776884V2.19817C6.09375 2.34332 5.53152 2.57563 5.01308 2.88734L4.01148 1.88314C3.94083 1.81232 3.84493 1.77249 3.7449 1.77242C3.64486 1.77236 3.54891 1.81207 3.47817 1.8828L1.8828 3.47817C1.81207 3.54891 1.77236 3.64486 1.77242 3.7449C1.77249 3.84493 1.81232 3.94083 1.88314 4.01148L2.88734 5.01308C2.57563 5.53152 2.34332 6.09375 2.19817 6.68102H0.776884C0.56875 6.68102 0.400024 6.84974 0.400024 7.05788V8.94217C0.400024 9.15031 0.56875 9.31903 0.776884 9.31903H2.19817C2.34332 9.90629 2.57563 10.4685 2.88734 10.987L1.88314 11.9886C1.81232 12.0592 1.77249 12.1551 1.77242 12.2552C1.77236 12.3552 1.81207 12.4511 1.8828 12.5219L3.47817 14.1172C3.54891 14.188 3.64486 14.2277 3.7449 14.2276C3.84493 14.2276 3.94083 14.1877 4.01148 14.1169L5.01308 13.1127C5.53152 13.4244 6.09375 13.6567 6.68102 13.8019V15.2232C6.68102 15.4313 6.84974 15.6 7.05788 15.6H8.94217C9.15031 15.6 9.31903 15.4313 9.31903 15.2232V13.8019C9.90629 13.6567 10.4685 13.4244 10.987 13.1127L11.9886 14.1169C12.0592 14.1877 12.1551 14.2276 12.2552 14.2276C12.3552 14.2277 12.4511 14.188 12.5219 14.1172L14.1172 12.5219C14.188 12.4511 14.2277 12.3552 14.2276 12.2552C14.2276 12.1551 14.1877 12.0592 14.1169 11.9886L13.1127 10.987C13.4244 10.4685 13.6567 9.90629 13.8019 9.31903H15.2232C15.4313 9.31903 15.6 9.15031 15.6 8.94217V7.05788C15.6 6.84974 15.4313 6.68102 15.2232 6.68102H13.8019C13.6567 6.09375 13.4244 5.53152 13.1127 5.01308L14.1169 4.01148C14.1877 3.94083 14.2276 3.84493 14.2276 3.7449C14.2277 3.64486 14.188 3.54891 14.1172 3.47817L12.5219 1.8828C12.4511 1.81207 12.3552 1.77236 12.2552 1.77242C12.1551 1.77249 12.0592 1.81232 11.9886 1.88314L10.987 2.88734C10.4685 2.57563 9.90629 2.34332 9.31903 2.19817V0.776884C9.31903 0.56875 9.15031 0.400024 8.94217 0.400024H7.05788ZM5.36201 8.00002C5.36201 6.54309 6.54309 5.36201 8.00002 5.36201C9.45696 5.36201 10.638 6.54309 10.638 8.00002C10.638 9.45696 9.45696 10.638 8.00002 10.638C6.54309 10.638 5.36201 9.45696 5.36201 8.00002Z" fill="#D2D8DE"/>
                </svg>
                <svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <g clip-path="url(#clip0_5101_42260)">
                    <path d="M7.58329 11.6667C8.35656 11.6658 9.09789 11.3582 9.64467 10.8114C10.1914 10.2646 10.499 9.52327 10.5 8.75001V3.64176C10.5009 3.33514 10.4409 3.03138 10.3235 2.7481C10.2062 2.46483 10.0338 2.20766 9.81629 1.99151L8.50846 0.683677C8.29231 0.466195 8.03514 0.293778 7.75187 0.176422C7.46859 0.0590653 7.16483 -0.000897138 6.85821 1.01439e-05H4.08329C3.31003 0.000936394 2.5687 0.308525 2.02192 0.855305C1.47514 1.40209 1.16755 2.14341 1.16663 2.91668V8.75001C1.16755 9.52327 1.47514 10.2646 2.02192 10.8114C2.5687 11.3582 3.31003 11.6658 4.08329 11.6667H7.58329ZM2.33329 8.75001V2.91668C2.33329 2.45255 2.51767 2.00743 2.84586 1.67924C3.17404 1.35105 3.61916 1.16668 4.08329 1.16668C4.08329 1.16668 6.95271 1.17484 6.99996 1.18068V2.33334C6.99996 2.64276 7.12288 2.93951 7.34167 3.1583C7.56046 3.37709 7.85721 3.50001 8.16663 3.50001H9.31929C9.32513 3.54726 9.33329 8.75001 9.33329 8.75001C9.33329 9.21414 9.14892 9.65926 8.82073 9.98745C8.49254 10.3156 8.04742 10.5 7.58329 10.5H4.08329C3.61916 10.5 3.17404 10.3156 2.84586 9.98745C2.51767 9.65926 2.33329 9.21414 2.33329 8.75001ZM12.8333 4.66668V11.0833C12.8324 11.8566 12.5248 12.5979 11.978 13.1447C11.4312 13.6915 10.6899 13.9991 9.91663 14H4.66663C4.51192 14 4.36354 13.9386 4.25415 13.8292C4.14475 13.7198 4.08329 13.5714 4.08329 13.4167C4.08329 13.262 4.14475 13.1136 4.25415 13.0042C4.36354 12.8948 4.51192 12.8333 4.66663 12.8333H9.91663C10.3808 12.8333 10.8259 12.649 11.1541 12.3208C11.4823 11.9926 11.6666 11.5475 11.6666 11.0833V4.66668C11.6666 4.51197 11.7281 4.36359 11.8375 4.2542C11.9469 4.1448 12.0953 4.08334 12.25 4.08334C12.4047 4.08334 12.553 4.1448 12.6624 4.2542C12.7718 4.36359 12.8333 4.51197 12.8333 4.66668Z" fill="#AFB6C1"/>
                  </g>
                  <defs>
                    <clipPath id="clip0_5101_42260">
                      <rect width="14" height="14" fill="white"/>
                    </clipPath>
                  </defs>
                </svg>
                <svg id="delete" width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path fill-rule="evenodd" clip-rule="evenodd" d="M3.36363 1.77778C3.36363 1.34822 3.72994 1 4.18181 1H11.8182C12.2701 1 12.6364 1.34822 12.6364 1.77778C12.6364 2.20733 12.2701 2.55556 11.8182 2.55556H4.18181C3.72994 2.55556 3.36363 2.20733 3.36363 1.77778ZM2.81818 5.66667H2V4.11111H14V5.66667H13.1818V12.1481C13.1818 13.7232 11.8387 15 10.1818 15H5.81818C4.16132 15 2.81818 13.7232 2.81818 12.1481V5.66667ZM11.5455 5.66667H4.45455V12.1481C4.45455 12.8641 5.06508 13.4444 5.81818 13.4444H10.1818C10.9349 13.4444 11.5455 12.8641 11.5455 12.1481V5.66667Z" fill="#D2D8DE"/>
                </svg>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div v-else-if="selectedTab === 'discounts' && isCreatingPromoCode" class="discounts_second">
        <div class="discounts_second_main">
          <div class="transition_1">
            <div @click="cancelCreatingPromoCode" class="employesss-link_1">Скидки и промокоды</div>
            <div class="arrow-container_1">
              <img src="../../static/img/arrow-right.png" alt="Стрелка вправо" class="arrow-icon_1">
            </div>
            <p class="creation_text_1">Создание промо-акции</p>
          </div>
        </div>
        <div class="discounts_second_container">
          <div class="discounts_second_wrapper">
            <p class="discounts_second_head">Создание промо-акции</p>
            <div class="discounts_second_content">
              <p class="discounts_second_label">Название в панели управления</p>
              <input type="text" name="" id="" placeholder="Акция для клиентов"> 
            </div>
            <div class="discounts_second_content">
              <p class="discounts_second_label">Название для клиентов</p>
              <input type="text" name="" id="" placeholder="Скидка 50%"> 
            </div>
            <div class="discounts_second_calendar">
              <div class="discounts_second_calendar_left">
                <p class="discounts_second_label">Дата начала</p>
                <input type="date">
              </div>
              <div class="discounts_second_calendar_right">
                <p class="discounts_second_label">Дата окончания</p>
                <input type="date">
              </div>
            </div>
            <div class="mark_container">
              <div class="mark" v-if="!Mark" @click="toggleMark"></div>
              <div class="mark_active" v-else @click="toggleMark">
                <svg width="14" height="14" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path fill-rule="evenodd" clip-rule="evenodd" d="M16.2556 6.15492L9.05226 14.4665L4.29285 9.7071L5.70706 8.29289L8.94764 11.5335L14.7443 4.84506L16.2556 6.15492Z" fill="#FFFFFF"/>
                </svg>
              </div>
              <p :class="{'mark_text_active': Mark, 'mark_text': !Mark}">Поставить текущую дату начала действия промокода при выдаче</p>
            </div>
          </div>
          <div class="discounts_second_wrapper">
            <p class="discounts_second_head">Настройка промокода</p>
            <div class="discounts_second_content">
              <p class="discounts_second_label">Название промокода</p>
              <input type="text" v-model="promoCode" :maxlength="maxLength" placeholder="ASDQWERTY-SK">
              <p class="discounts_second_sublabel">Для ввода доступно — {{ remainingChars }}/{{ maxLength }}</p>
            </div>
            <div class="discounts_second_content">
              <p class="discounts_second_label">Размер скидки</p>
              <input type="text" name="" id="" placeholder="Скидка 50%"> 
            </div>
            <div class="discounts_second_content">
              <p class="discounts_second_label">Количество активаций</p>
              <input type="text" name="" id="" placeholder="50"> 
            </div>
            <button class="discounts_second_btn">Создать промокод</button>
          </div>
        </div>
      </div>
      <div class="custom" v-if="selectedTab === 'custom'">
        <div class="custom_head">
          <p class="custom_text">Код перед &lt;/head&gt; </p>
          <textarea class="custom_input" name="" id="" cols="30" rows="10" v-model="symbols2" maxlength="2000"></textarea>
          <p class="custom_subtext">{{ symbols2.length }} / 2000</p>
        </div>
        <div class="custom_head">
          <p class="custom_text">Код перед &lt;/body&gt; </p>
          <textarea class="custom_input" name="" id="" cols="30" rows="10" v-model="symbols" maxlength="2000"></textarea>
          <p class="custom_subtext"> {{ symbols.length }} / 2000</p>
        </div>
        <HighCode
        ref="H"
        class="code"
        :codeValue="value"
        theme="light"
        :nameShow="false"
        :copy="false"
        :lang="HTML"
        :textEditor="true"
        v-model="symbols"
        maxlength="2000"></HighCode>
        <div class="custom_btn">
          <button class="custom_save">Сохранить</button>
          <button class="custom_exit">Отмена</button>
        </div>

      </div>
      <WidgetConstructor v-if="selectedTab != 'telegram' && selectedTab != 'integrations' && selectedTab != 'discounts'" v-bind:theme="switches.theme" :MainColor="widget.Main" :WidgetColor="widget.Back" :BakcgroundColor="widget.Plashka" :TextColor="widget.Text"/>
    </div>
    
  </div>
</template>
  
<script>
import WidgetConstructor from './WidgetConstructor.vue';
import PalitraPage from './PalitraPage.vue';
import SelectPage from '../components/SelectPage.vue';
import { HighCode } from 'vue-highlight-code';
import 'vue-highlight-code/dist/style.css';
import axios from 'axios';

export default {
  components: { WidgetConstructor , PalitraPage, SelectPage, HighCode} ,
  data() {
    return {
      promoCode: '',
      maxLength: 15,
      Mark: false,
      isCreatingPromoCode: false,
      telegramToken: '',
      selectedImages: [],
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
      symbols: "",
      symbols2: "",
      symbols3: "",
      symbols4: "",
      selectedChoice: null, 
      isCircleShown1: false,
      isCircleShown2: false, 
      isCircleShown3: false, 
      isCircleShown4: false,

      widget:{
        Main: '#6266EA',
        Back: '#FFFFFF',
        Plashka: '#FAFAFA',
        Text: '#535C69',
      },

      widgetDesign: '',
      widgetLink: 'https://calendar.com/' + 'user' + '/' + 'widgetname',

      chips: [],
    };
  },
  mounted() {
    // После монтирования компонента выбираем первую вкладку по умолчанию
    this.$refs.tabs.querySelectorAll('.tab-link')[0].click();
  },
  computed: {
    filteredChips() {
      // Начинаем с индекса 1 (второй элемент) и возвращаем оставшиеся элементы
      return this.chips.slice(1);
    },
    remainingChars() {
      return this.maxLength - this.promoCode.length;
    },
  },
  methods: {
    toggleMark() {
      this.Mark = !this.Mark;
    },
    startCreatingPromoCode() {
      this.isCreatingPromoCode = true;
    },
    cancelCreatingPromoCode() {
      this.isCreatingPromoCode = false;
    },
    deleteChip(chip){
      let indexToRemove = this.chips.indexOf(chip);
      if (indexToRemove !== -1) {
        this.chips.splice(indexToRemove, 1);
      }
    },
    async get_uslugi(filials){
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/uslugi_fromfilials/?variable=${filials}`);
        this.uslugi = response.data; // Присваиваем полученные данные массиву uslugi
        this.uslugi.reverse();
        this.uslugiLoaded = true; // Устанавливаем флаг загрузки в true sd
      } catch (error) {
        console.error('Error fetching uslugi:', error);
      }
    },
    handleSelectInput(selected) {
      const existingChip = this.chips.find(chip => chip.name === selected.name && chip.id === selected.id);
      if (!existingChip) {
        this.chips.push({ name: selected.name, id: selected.id });
        var chipIds = this.chips.map(chip => chip.id);
        var string = chipIds.join(',');
        this.get_uslugi(string)
      }
    },

    async handleColorUpdate(color, additionalArgument) {
      switch (additionalArgument) {
        case 1: { this.widget.Main = color; break; }
        case 2: { this.widget.Back = color; break; }
        case 3: { this.widget.Plashka = color; break; }
        case 4: { this.widget.Text = color; break; }
      }
      setTimeout(() => {
        this.closeall();
      }, 0);
    },

    save(){
      const formData = new FormData();
      formData.append('language', this.selectedLanguage);
      formData.append('link', this.widgetLink);
      formData.append('design', this.widgetDesign);
      formData.append('text', this.widget.Text);
      formData.append('plashka', this.widget.Plashka);
      formData.append('back', this.widget.Back);
      formData.append('main', this.widget.Main);
      formData.append('theme', this.switches.theme);
      formData.append('ogranichenie', this.selectedOgranichenie);
      formData.append('interval', this.selectedInterval);
      formData.append('cancellation', this.switches.cancellation);
      formData.append('employee', this.switches.employee);
      formData.append('company', this.switches.company);
      formData.append('fedback', this.switches.feedback);
      formData.append('branches', this.chips);
      formData.append('vklink', this.widgetLinkVk)
      formData.append('isvk', this.switches.vkontakte,);
      formData.append('whatsapplink', this.widgetLinkWhatsApp);
      formData.append('iswhatsapp', this.switches.whatsapp);
      formData.append('instagramlink', this.widgetLinkInstagram);
      formData.append('isinstagram', this.switches.instagram);
      formData.append('telegramlink', this.widgetLinkTelegram);
      formData.append('istelegram', this.switches.telegram);
      formData.append('name', this.widgetName);      
      formData.append('buttonname', this.widgetName) ///ОТРЕДАЧИТЬ
      formData.append('telegramtoken', this.widgetName) ///ОТРЕДАЧИТЬ
      formData.append('hellomessage', this.widgetName) ///ОТРЕДАЧИТЬ

      this.selectedImages.forEach(image => {formData.append('images[]', image);});
      axios.post('http://127.0.0.1:8000/api/widget_create/', formData)
      .then(response => {
        // Обработка успешного ответа
        console.log(response);
      })
      .catch(error => {
        // Обработка ошибок
        console.error('Error while posting formData:', error);
      });
    },

    themechange(){
      if (this.switches.theme) {
        this.widget.Main = '#FFC25A'
        this.widget.Back = '#222433'
        this.widget.Plashka = '#1A1B27'
        this.widget.Text = '#F5F5F5'
      }else{
        this.widget.Main = '#6266EA'
        this.widget.Back = '#FFFFFF'
        this.widget.Plashka = '#FAFAFA'
        this.widget.Text = '#535C69'
      }
    },

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
      // Обновляем src изображения
      event.target.closest('.img_plus').querySelector('img').src = e.target.result;
      // Добавляем выбранное изображение в переменную selectedImages
      this.selectedImages.push(file);
    };
    reader.readAsDataURL(file);
  }
},
    toggleSelection(num) {
      switch(num){
        case 1:{ this.isCircleShown1=true;this.isCircleShown2=false;this.isCircleShown3=false;this.isCircleShown4=false;break}
        case 2:{ this.isCircleShown2=true;this.isCircleShown1=false;this.isCircleShown3=false;this.isCircleShown4=false;break}
        case 3:{ this.isCircleShown3=true;this.isCircleShown2=false;this.isCircleShown1=false;this.isCircleShown4=false;break}
        case 4:{ this.isCircleShown4=true;this.isCircleShown2=false;this.isCircleShown3=false;this.isCircleShown1=false;break}
      }
    },
    closeall(){
      this.isCircleShown1=false;
      this.isCircleShown2=false;
      this.isCircleShown3=false;
      this.isCircleShown4=false;
    },
    selectTab(tab) {
      this.selectedTab = tab; // Функция для изменения выбранной вкладки
    },
    activateChoice(event) {
      const choice = event.currentTarget;
      const choiceType = choice.getAttribute('data-type');

      this.widgetDesign = choiceType;
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
.tg-row{
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.textarea_subtitle{
  color: #AFB6C1;
  font-size: 14px;
  margin-top: 0;
}
.symbols_counter{
  color: #AFB6C1;
  font-size: 14px;
}


    .chip svg:hover path{
    fill: rgb(250, 148, 148);
  }
  .chips-block{
    width: 100%;
    display: flex;
    gap: 5px;
    flex-wrap: wrap;
    margin-top: 10px;
  }

  .chip{
    display: flex;
    gap: 5px;
    align-items: center;
    justify-content: start;
    background-color: #6266EA;
    height: 20px;
    padding: 0 15px;
    border-radius: 10px;
    transition: all .2s ease;
  }

  .chip:hover{
    background-color: #5357c7;
    cursor: pointer;
  }

  .chip p{
    margin: 0;
    color: white;
    font-family: 'TT Norms';
    font-size: 12px;
    margin-top: -1.5px;
  }
  .descr{
    font-family: TT Norms Medium;
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
    margin-right: 20px;
  }
  
  .settings {
    width: 100%;
    text-align: center;
    height: auto;
    background-color: #FFFFFF;
    padding: 20px;
    border-radius: 5px;
  }
  
  label {
    margin-right: 10px;
    margin-bottom: 10px;
    font-family: TT Norms Medium;
    font-size: 13px;
    line-height: 15px;
    letter-spacing: 0em;
  }
  
  input {
    margin-bottom: 0;
    margin-right: 10px;
  }
  
  p{
    text-align: left;
    font-family: TT Norms Medium;
    font-size: 14px;
    line-height: 17px;
    color:#535C69;
    margin: 10px 0;
  }

  input::placeholder {
    font-family: "TT Norms Medium";
    font-size: 13px;
    font-weight: 500;
    line-height: 17px;
    letter-spacing: 0em;
    color: #D2D8DE;
  }
  
  select {
    width: 100%;
    padding: 8px 10px;
    font-family: TT Norms Medium;
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
    font-family: TT Norms Medium;
    font-size: 14px;
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
    font-family: TT Norms Medium;
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

  .img_plus:hover{
    cursor: pointer;
    background-color: rgb(248, 248, 248);
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
    height: auto;
    width: 120px;
    border-radius: 3px;
    padding: 5px 10px;
    border: 1px solid #D2D8DE;
    display: flex;
    gap: 10px;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    position: relative;
  }

  .rgb:hover{
    cursor: pointer;
    background-color: rgb(248, 248, 248);
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
    font-family: TT Norms Medium;
    font-size: 12px;
    font-weight: 500;
    line-height: 10px;
    letter-spacing: 0em;
    text-align: left;
    color: #535C69;
    margin: 0;
  }
  .dark{
    font-family: TT Norms Medium;
    font-size: 12px;
    font-weight: 500;
    line-height: 10px;
    letter-spacing: 0em;
    text-align: left;
    color: #AFB6C1;    
    margin: 0;
  }
  .window{
    width: 100%;
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
    border: 1px solid #DDE1E5;
    transition: all 0.2s ease;
  }
  .cancel-button:hover{
    color: #5357c7;
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
    display: flex;
    justify-content: start;
    background: #FAFAFA;
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
    font-family: TT Norms Medium;
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
  .custom{
    padding: 30px;
    width: 50%;
    display: flex;
    flex-direction: column;
    gap: 20px;
  }
  .custom_head{
    display: flex;
    flex-direction: column;
    gap: 5px;
  }
  .custom_text{
    font-family: TT Norms Medium;
    font-size: 14px;
    line-height: 16.52px;
    text-align: left;
    color: #535C69;
    margin: 0;
  }
  .custom_input::placeholder{
    color: #AFB6C1;
    font-family: TT Norms Medium;
    font-size: 14px;
  }
  .custom_input{
    font-size: 14px;
    font-family: TT Norms Medium;
    color: #535C69;
    padding: 10px;
    border-radius: 3px;
    border: 1px solid #C6CBD2;
    background: #FFFFFF;
    width: 100%;
    resize: none;
    outline: none;
  }
  .custom_subtext{
    font-family: TT Norms Medium;
    font-size: 14px;
    line-height: 16.52px;
    text-align: left;
    color: #AFB6C1;
    margin: 0;
  }
  .custom_btn{
    display: flex;
    gap: 20px;
  }
  .custom_save{
    color: #6266EA;
    background: #EFEFFF;
  }
  .custom_save:hover{
    color: #6266EA;
    background: #DBEAFF;
  }
  .custom_exit{
    color: #535C69;
    background: #FFFFFF;
    border: 1px solid #DDE1E5;
  }
  .custom_exit:hover{
    color: #6266EA;
  }
  .telegram{
    display: flex;
    flex-direction: column;
    gap: 20px;
  }
  .telegram_description{
    margin-top: 30px;
  }
  .telegram_description ol{
    text-align: left;
    color: #AFB6C1;
    font-family: TT Norms Medium;
    padding-left: 1em;
    font-size: 13px;
  }
  .telegram_main{
    border-radius: 5px;
    width: 100%;
    padding: 20px;
    height: fit-content;
    background: #FFFFFF;
  }
  .telegram_header{
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  .telegram_button-disabled{
    background: #FAFAFA;
    font-family: TT Norms Medium;
    font-size: 13px;
    line-height: 16.9px;
    text-align: left;
    color: #D2D8DE;
    width: fit-content;
    cursor: default;
  }
  .telegram_button-active{
    background: #EFEFFF;
    font-family: TT Norms Medium;
    font-size: 13px;
    line-height: 16.9px;
    text-align: left;
    color: #6266EA;
    width: fit-content;
    cursor: pointer;
  }
  .telegram_label{
    font-family: TT Norms Medium;
    font-size: 13px;
    line-height: 15.34px;
    text-align: left;
    color: #535C69;
    margin-bottom: 5px;
  }
  .discounts{
    width: 80%;
  }
  .integrations{
    width: 80%;
  }
  .discounts_header{
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  .integrations_header{
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  .discounts_input{
    width: 30%;
    border: 1px solid #C6CBD2;
  }
  .integrations_input{
    width: 30%;
    border: 1px solid #C6CBD2;
  }
  .discounts_nav_container{
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    grid-template-rows: 1fr;
  }
  .integrations_nav_container{
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    grid-template-rows: 1fr;
  }
  .discounts_nav_text{
    font-family: TT Norms Medium;
    font-size: 14px;
    line-height: 16.52px;
    text-align: left;
    color: #7D838C;
  }
  .integrations_nav_text{
    font-family: TT Norms Medium;
    font-size: 14px;
    line-height: 16.52px;
    text-align: left;
    color: #7D838C;
  }
  .divider {
    border-bottom: 1px solid rgba(50, 56, 74, 0.1); 
    width: auto;
    margin: 0;
  }
  .discounts_new{
    padding: 20px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    background: #EFEFFF;
    border-radius: 5px;
  }
  .integrations_new{
    padding: 20px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    background: #EFEFFF;
    border-radius: 5px;
  }
  .discounts_new_header{
    font-family: TT Norms light;
    font-size: 16px;
    line-height: 22.4px;
    text-align: left;
    color: #000000;
  }
  .integrations_new_header{
    font-family: TT Norms light;
    font-size: 16px;
    line-height: 22.4px;
    text-align: left;
    color: #000000;
  }
  .discounts_new_btn{
    display: flex;
  }
  .integrations_new_btn{
    display: flex;
  }
  .ponyatno{
    background: none;
    color: #6266EA;
    font-family: TT Norms Light;
    font-size: 13px;
    line-height: 15.34px;
    text-align: left;
  }
  .discounts_new_container{
    display: flex;
    justify-content: space-between;
  }
  .integrations_new_container{
    display: flex;
    justify-content: space-between;
  }
  .krest{
    font-size: 16px;
  }
  .discounts_main{
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    grid-template-rows: 1fr;    
  }
  .integrations_main{
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    grid-template-rows: 1fr;    
  }
  .discounts_main_text{
    font-family: TT Norms light;
    font-size: 14px;
    line-height: 16.52px;
    text-align: left;
    color: #7D838C;
  }
  .integrations_main_text{
    font-family: TT Norms light;
    font-size: 14px;
    line-height: 16.52px;
    text-align: left;
    color: #7D838C;
  }
  .discounts_main_items_container{
    display: flex;
    align-items: center;
    gap: 25px;
  }
  .integrations_main_items_container{
    display: flex;
    align-items: center;
    gap: 25px;
  }
  .discounts_main_items{
    display: flex;
    gap: 10px;
  }
  .integrations_main_items{
    display: flex;
    gap: 10px;
  }
  .transition_1 {
    display: flex;
    flex-direction: row;
    gap: 5px;
    margin: 20px 0;
  } 
  
  .employesss-link_1 {
    font-family: 'TT Norms Medium';
    font-size: 14px;
    line-height: 14px;
    text-align: left;
    text-decoration: none;
    color: #D2D8DE;
    cursor: pointer;
    transition: all 0.3s ease;
  }
  
  .creation_text_1 {
    color: #AFB6C1;
    font-family: 'TT Norms Medium';
    font-size: 14px;
    line-height: 14px;
    letter-spacing: 0em;
    text-align: left;
    margin: 0;
  }
  
  .arrow-container_1 {
    display: flex;
    align-items: center;
  }
  
  .arrow-icon_1 {
    height: 50%;
  }
  .discounts_first{
    display: flex;
    flex-direction: column;
    gap: 20px;
    background: #FFFFFF;
    padding: 30px;
  }
  .integrations_first{
    display: flex;
    flex-direction: column;
    gap: 20px;
    background: #FFFFFF;
    padding: 30px;
  }
  .employesss-link_1:hover{
    color: #535C69;
  }
  .discounts_second_head{
    font-family: TT Norms Medium;
    font-size: 20px;
    line-height: 23.6px;
    text-align: left;
    color: #535C69;
  }
  .discounts_second_wrapper{
    display: flex;
    flex-direction: column;
    gap: 20px;
    padding: 30px;
    background: #FFFFFF;
    border-radius: 5px;
    width: 100%;
  }
  .discounts_second_content{
    display: flex;
    flex-direction: column;
  }
  .discounts_second_label{
    font-family: TT Norms Medium;
    font-size: 13px;
    line-height: 15.34px;
    text-align: left;
    color: #535C69;
  }
  .discounts_second_calendar{
    display: flex;
    justify-content: space-between;
    gap: 25px;
  }
  .mark_text{
    font-family: TT Norms Medium;
    font-size: 14px;
    line-height: 16.52px;
    text-align: left;
    color: #C6CBD2;
  }
  .mark_text_active {
    color: #535C69;
  }
  .mark_container{
    display: flex;
    gap: 5px;
    align-items: center;
  }
  .mark{
    width: 22px;
    height: 16px;
    border-radius: 3px;
    cursor: pointer;
    user-select:none;
    background: #F3F5F6;
  }
  .mark_active{
    display: flex;
    justify-content: center;
    align-items: center;
    width: 16px;
    height: 16px;
    border-radius: 3px;
    border: 1px solid #C6CBD2;
    cursor: pointer;
    background: #6266EA;
    user-select:none;
  }
  .discounts_second_container{
    display: flex;
    gap: 20px;
  }
  .discounts_second_sublabel{
    font-family: TT Norms Medium;
    font-size: 12px;
    line-height: 14.16px;
    text-align: left;
    color: #AFB6C1;
  }
  .discounts_second_btn{
    width: 50%;
    background: #EFEFFF;
    color: #6266EA;
    transition: all 0.3s ease;
  }
  .discounts_second_btn:hover{
    background: #464AD9;
    color: #FFFFFF;
  }
  @media (max-width: 768px){
    .main{
      padding: 20px;
    }
    #lightmode{
      display: none;
    }
    .window{
      width: 100%;
    }
  }
  </style>