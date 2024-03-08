<template>
  <div class="main">
    <img src="../../static/img/widget.png" alt="" class="img_head">
    <div class="branch" v-if="currentPage === 'branch'">
      <div class="search">
        <input type="text" placeholder="Введите название улицы или филиала">
      </div>
      <div class="card">
        <img src="../../static/img/map.png" alt="">
        <div class="card_container">
          <p class="card_name">Nomad Barbershop №1 на Сатпаева 253/1</p>
          <div class="card_address_container">
            <svg width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd" clip-rule="evenodd" d="M1.2002 4.78875C1.2002 2.11449 3.31968 0 6.0002 0C8.61838 0 10.8002 2.17669 10.8002 4.78875C10.8002 8.00081 6.0002 12 6.0002 12C6.0002 12 1.2002 8.063 1.2002 4.78875ZM6.0002 6.6C6.99431 6.6 7.8002 5.79411 7.8002 4.8C7.8002 3.80589 6.99431 3 6.0002 3C5.00608 3 4.2002 3.80589 4.2002 4.8C4.2002 5.79411 5.00608 6.6 6.0002 6.6Z" fill="#AFB6C1"/>
            </svg>
            <p class="card_address">г. Павлодар, ул. Сатпаева 253/1</p>
          </div>
          <div class="card_time_container">
            <svg width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd" clip-rule="evenodd" d="M12 6C12 9.31371 9.31371 12 6 12C2.68629 12 0 9.31371 0 6C0 2.68629 2.68629 0 6 0C9.31371 0 12 2.68629 12 6ZM6.3 2.7H5.1V5.94853L8.27574 9.12426L9.12426 8.27574L6.3 5.45147V2.7Z" fill="#AFB6C1"/>
            </svg>
            <p class="card_time">Ближайшая свободная запись: сегодня в 18:30</p>
          </div>
        </div>
      </div>
      <div class="card">
        <img src="../../static/img/map.png" alt="">
        <div class="card_container">
          <p class="card_name">Nomad Barbershop №1 на Сатпаева 253/1</p>
          <div class="card_address_container">
            <svg width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd" clip-rule="evenodd" d="M1.2002 4.78875C1.2002 2.11449 3.31968 0 6.0002 0C8.61838 0 10.8002 2.17669 10.8002 4.78875C10.8002 8.00081 6.0002 12 6.0002 12C6.0002 12 1.2002 8.063 1.2002 4.78875ZM6.0002 6.6C6.99431 6.6 7.8002 5.79411 7.8002 4.8C7.8002 3.80589 6.99431 3 6.0002 3C5.00608 3 4.2002 3.80589 4.2002 4.8C4.2002 5.79411 5.00608 6.6 6.0002 6.6Z" fill="#AFB6C1"/>
            </svg>
            <p class="card_address">г. Павлодар, ул. Сатпаева 253/1</p>
          </div>
          <div class="card_time_container">
            <svg width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd" clip-rule="evenodd" d="M12 6C12 9.31371 9.31371 12 6 12C2.68629 12 0 9.31371 0 6C0 2.68629 2.68629 0 6 0C9.31371 0 12 2.68629 12 6ZM6.3 2.7H5.1V5.94853L8.27574 9.12426L9.12426 8.27574L6.3 5.45147V2.7Z" fill="#AFB6C1"/>
            </svg>
            <p class="card_time">Ближайшая свободная запись: сегодня в 18:30</p>
          </div>
        </div>
      </div>
      <div class="card_next">
        <div class="card_next_container">
          <p class="card_next_text">Выбор филиала</p>
          <div class="divider"></div>
          <p class="card_next_subtext">Всего <span class="card_number">6</span> филиалов</p>
        </div>
        <div class="card_btn">
          <button class="card_next_btn" @click="showChoice">Продолжить</button>
        </div>
      </div>        
    </div>
    <div class="choice" v-else-if="currentPage === 'choice'">
      <div class="choice_overview ">
        <div class="choice_rate_container">
          <p class="choice_rate">3.7</p>
          <div class="choice_star_container">
            <div class="stars">
              <svg width="18" height="17" viewBox="0 0 18 17" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" clip-rule="evenodd" d="M12.2575 5.95727C11.7944 5.95727 11.3874 5.66134 11.2602 5.2321L11.2426 5.1728C11.2405 5.16555 11.2382 5.15833 11.2359 5.15112L9.7288 0.469756C9.7288 0.469756 9.7288 0.469756 9.7288 0.469756C9.53202 -0.141467 8.64216 -0.1614 8.41615 0.440352C8.41615 0.440352 8.41615 0.440352 8.41615 0.440352L6.65496 5.12944C6.64683 5.15109 6.63948 5.17301 6.63292 5.19515L6.62196 5.23211C6.49474 5.66134 6.08776 5.95727 5.62468 5.95727H5.582H0.693556C0.693556 5.95727 0.693556 5.95727 0.693556 5.95727C0.0294735 5.95727 -0.253536 6.77131 0.276429 7.15708C0.276429 7.15708 0.27643 7.15708 0.276429 7.15708L4.37907 10.1434C4.39527 10.1552 4.41183 10.1666 4.42873 10.1774L4.48064 10.2108C4.85591 10.452 5.02647 10.8993 4.90256 11.3174L4.87737 11.4024C4.87568 11.4081 4.87393 11.4138 4.87213 11.4195L3.37747 16.1422C3.18269 16.7577 3.92148 17.2519 4.45137 16.8606L8.27591 14.0367C8.28719 14.0284 8.29829 14.0198 8.30921 14.011L8.33601 13.9895C8.72065 13.6805 9.27936 13.6805 9.66399 13.9895L9.6908 14.011C9.70171 14.0198 9.71282 14.0284 9.7241 14.0367L13.5486 16.8606C14.0785 17.2519 14.8173 16.7577 14.6225 16.1422L13.1279 11.4195C13.1261 11.4138 13.1243 11.4081 13.1226 11.4024L13.0974 11.3174C12.9735 10.8993 13.1441 10.452 13.5194 10.2108L13.5713 10.1774C13.5882 10.1666 13.6047 10.1552 13.6209 10.1434L17.7236 7.15708C17.7236 7.15708 17.7236 7.15708 17.7236 7.15708C18.2535 6.77131 17.9705 5.95727 17.3064 5.95727H12.3001H12.2575Z" fill="#F7D37D"/>
              </svg>
              <svg width="18" height="17" viewBox="0 0 18 17" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" clip-rule="evenodd" d="M12.2575 5.95727C11.7944 5.95727 11.3874 5.66134 11.2602 5.2321L11.2426 5.1728C11.2405 5.16555 11.2382 5.15833 11.2359 5.15112L9.7288 0.469756C9.7288 0.469756 9.7288 0.469756 9.7288 0.469756C9.53202 -0.141467 8.64216 -0.1614 8.41615 0.440352C8.41615 0.440352 8.41615 0.440352 8.41615 0.440352L6.65496 5.12944C6.64683 5.15109 6.63948 5.17301 6.63292 5.19515L6.62196 5.23211C6.49474 5.66134 6.08776 5.95727 5.62468 5.95727H5.582H0.693556C0.693556 5.95727 0.693556 5.95727 0.693556 5.95727C0.0294735 5.95727 -0.253536 6.77131 0.276429 7.15708C0.276429 7.15708 0.27643 7.15708 0.276429 7.15708L4.37907 10.1434C4.39527 10.1552 4.41183 10.1666 4.42873 10.1774L4.48064 10.2108C4.85591 10.452 5.02647 10.8993 4.90256 11.3174L4.87737 11.4024C4.87568 11.4081 4.87393 11.4138 4.87213 11.4195L3.37747 16.1422C3.18269 16.7577 3.92148 17.2519 4.45137 16.8606L8.27591 14.0367C8.28719 14.0284 8.29829 14.0198 8.30921 14.011L8.33601 13.9895C8.72065 13.6805 9.27936 13.6805 9.66399 13.9895L9.6908 14.011C9.70171 14.0198 9.71282 14.0284 9.7241 14.0367L13.5486 16.8606C14.0785 17.2519 14.8173 16.7577 14.6225 16.1422L13.1279 11.4195C13.1261 11.4138 13.1243 11.4081 13.1226 11.4024L13.0974 11.3174C12.9735 10.8993 13.1441 10.452 13.5194 10.2108L13.5713 10.1774C13.5882 10.1666 13.6047 10.1552 13.6209 10.1434L17.7236 7.15708C17.7236 7.15708 17.7236 7.15708 17.7236 7.15708C18.2535 6.77131 17.9705 5.95727 17.3064 5.95727H12.3001H12.2575Z" fill="#F7D37D"/>
              </svg>
              <svg width="18" height="17" viewBox="0 0 18 17" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" clip-rule="evenodd" d="M12.2575 5.95727C11.7944 5.95727 11.3874 5.66134 11.2602 5.2321L11.2426 5.1728C11.2405 5.16555 11.2382 5.15833 11.2359 5.15112L9.7288 0.469756C9.7288 0.469756 9.7288 0.469756 9.7288 0.469756C9.53202 -0.141467 8.64216 -0.1614 8.41615 0.440352C8.41615 0.440352 8.41615 0.440352 8.41615 0.440352L6.65496 5.12944C6.64683 5.15109 6.63948 5.17301 6.63292 5.19515L6.62196 5.23211C6.49474 5.66134 6.08776 5.95727 5.62468 5.95727H5.582H0.693556C0.693556 5.95727 0.693556 5.95727 0.693556 5.95727C0.0294735 5.95727 -0.253536 6.77131 0.276429 7.15708C0.276429 7.15708 0.27643 7.15708 0.276429 7.15708L4.37907 10.1434C4.39527 10.1552 4.41183 10.1666 4.42873 10.1774L4.48064 10.2108C4.85591 10.452 5.02647 10.8993 4.90256 11.3174L4.87737 11.4024C4.87568 11.4081 4.87393 11.4138 4.87213 11.4195L3.37747 16.1422C3.18269 16.7577 3.92148 17.2519 4.45137 16.8606L8.27591 14.0367C8.28719 14.0284 8.29829 14.0198 8.30921 14.011L8.33601 13.9895C8.72065 13.6805 9.27936 13.6805 9.66399 13.9895L9.6908 14.011C9.70171 14.0198 9.71282 14.0284 9.7241 14.0367L13.5486 16.8606C14.0785 17.2519 14.8173 16.7577 14.6225 16.1422L13.1279 11.4195C13.1261 11.4138 13.1243 11.4081 13.1226 11.4024L13.0974 11.3174C12.9735 10.8993 13.1441 10.452 13.5194 10.2108L13.5713 10.1774C13.5882 10.1666 13.6047 10.1552 13.6209 10.1434L17.7236 7.15708C17.7236 7.15708 17.7236 7.15708 17.7236 7.15708C18.2535 6.77131 17.9705 5.95727 17.3064 5.95727H12.3001H12.2575Z" fill="#F7D37D"/>
              </svg>
              <svg width="18" height="17" viewBox="0 0 18 17" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" clip-rule="evenodd" d="M13.1279 11.4195L14.6225 16.1422C14.8173 16.7577 14.0785 17.2519 13.5486 16.8606L9.7241 14.0367C9.33946 13.7277 8.66054 13.7277 8.27591 14.0367L4.45137 16.8606C3.92148 17.2519 3.18269 16.7577 3.37747 16.1422L4.87213 11.4195C4.99604 11.0014 4.75434 10.3846 4.37907 10.1434L0.276429 7.15708C-0.253536 6.77131 0.0294735 5.95727 0.693556 5.95727H5.582C6.04508 5.95727 6.52774 5.55867 6.65496 5.12944L8.41615 0.440352C8.64216 -0.1614 9.53202 -0.141467 9.7288 0.469756L11.2426 5.1728C11.3698 5.60204 11.8371 5.95727 12.3001 5.95727H17.3064C17.9705 5.95727 18.2535 6.77131 17.7236 7.15708L13.6209 10.1434C13.2457 10.3846 13.004 11.0014 13.1279 11.4195ZM13.0512 9.32131L16.2989 6.95727H12.3001C11.398 6.95727 10.5455 6.3166 10.2878 5.47017L9.04518 1.60965L7.60128 5.45397C7.46294 5.88503 7.17789 6.24179 6.86355 6.48962C6.53959 6.74502 6.09137 6.95727 5.582 6.95727H1.70114L4.94884 9.32131C5.34504 9.58694 5.6032 9.98792 5.74502 10.3532C5.88916 10.7246 5.97464 11.2187 5.83091 11.7036L5.8283 11.7124L4.63541 15.4817L7.66859 13.2421C8.07252 12.926 8.5664 12.8049 9 12.8049C9.43362 12.8049 9.9275 12.926 10.3314 13.2421L13.3646 15.4817L12.1717 11.7124L12.1691 11.7036C12.0254 11.2187 12.1108 10.7246 12.255 10.3532C12.3968 9.9879 12.655 9.58693 13.0512 9.32131Z" fill="#AFB6C1"/>
              </svg>
              <svg width="18" height="17" viewBox="0 0 18 17" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" clip-rule="evenodd" d="M13.1279 11.4195L14.6225 16.1422C14.8173 16.7577 14.0785 17.2519 13.5486 16.8606L9.7241 14.0367C9.33946 13.7277 8.66054 13.7277 8.27591 14.0367L4.45137 16.8606C3.92148 17.2519 3.18269 16.7577 3.37747 16.1422L4.87213 11.4195C4.99604 11.0014 4.75434 10.3846 4.37907 10.1434L0.276429 7.15708C-0.253536 6.77131 0.0294735 5.95727 0.693556 5.95727H5.582C6.04508 5.95727 6.52774 5.55867 6.65496 5.12944L8.41615 0.440352C8.64216 -0.1614 9.53202 -0.141467 9.7288 0.469756L11.2426 5.1728C11.3698 5.60204 11.8371 5.95727 12.3001 5.95727H17.3064C17.9705 5.95727 18.2535 6.77131 17.7236 7.15708L13.6209 10.1434C13.2457 10.3846 13.004 11.0014 13.1279 11.4195ZM13.0512 9.32131L16.2989 6.95727H12.3001C11.398 6.95727 10.5455 6.3166 10.2878 5.47017L9.04518 1.60965L7.60128 5.45397C7.46294 5.88503 7.17789 6.24179 6.86355 6.48962C6.53959 6.74502 6.09137 6.95727 5.582 6.95727H1.70114L4.94884 9.32131C5.34504 9.58694 5.6032 9.98792 5.74502 10.3532C5.88916 10.7246 5.97464 11.2187 5.83091 11.7036L5.8283 11.7124L4.63541 15.4817L7.66859 13.2421C8.07252 12.926 8.5664 12.8049 9 12.8049C9.43362 12.8049 9.9275 12.926 10.3314 13.2421L13.3646 15.4817L12.1717 11.7124L12.1691 11.7036C12.0254 11.2187 12.1108 10.7246 12.255 10.3532C12.3968 9.9879 12.655 9.58693 13.0512 9.32131Z" fill="#AFB6C1"/>
              </svg>            
            </div>
            <p class="choice_star_text">24 оценки</p>
          </div>
        </div>
        <div class="choice_info">
          <div class="choice_info_container">
            <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M1.25 5C1.25 2.44066 2.7056 1.51888 3.75412 1.3033C4.06243 1.23991 4.36115 1.39819 4.55 1.65L5.97962 3.55616C6.27821 3.95428 6.23862 4.51138 5.88673 4.86327L4.75965 5.99035C4.45529 6.29471 4.38168 6.75866 4.60979 7.12367C4.96976 7.69966 5.59983 8.59983 6.5 9.5C7.40017 10.4002 8.30034 11.0302 8.87633 11.3902C9.24134 11.6183 9.70529 11.5447 10.0097 11.2403L11.1367 10.1133C11.4886 9.76138 12.0457 9.72179 12.4438 10.0204L14.35 11.45C14.6018 11.6389 14.7601 11.9376 14.6967 12.2459C14.4811 13.2944 13.5593 14.75 11 14.75C8 14.75 5.75 12.5 4.625 11.375C3.5 10.25 1.25 8 1.25 5Z" fill="#535C69"/>
            </svg>
            <p class="choice_info_text">+ 7 (705) 356 55 55</p>
          </div>
          <div class="choice_info_container">
            <svg width="16" height="15" viewBox="0 0 16 15" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd" clip-rule="evenodd" d="M15.5 7.5C15.5 11.6421 12.1421 15 8 15C3.85786 15 0.5 11.6421 0.5 7.5C0.5 3.35786 3.85786 0 8 0C12.1421 0 15.5 3.35786 15.5 7.5ZM8.375 3.375H6.875V7.43566L10.8447 11.4053L11.9053 10.3447L8.375 6.81434V3.375Z" fill="#535C69"/>
            </svg>
            <p class="choice_info_text">Пн—Вс: с 9:00 до 20:00</p>
          </div>
        </div>
      </div>
      <div class="service">
        <div class="service_container">
          <p class="service_container_text">Выбрать услугу</p>
        </div>
        <div class="service_container">
          <p class="service_container_text">Выбрать<br>специалиста</p>
        </div>
      </div>
      <div class="card_next">
        <div class="card_next_container">
          <p class="card_next_text">Новая запись</p>
          <div class="divider"></div>
          <p class="card_next_subtext">Приступим</p>
        </div>
        <div class="card_btn">
          <button class="card_next_btn" @click="showFavor">Продолжить</button>
        </div>
      </div>
    </div>
    <div class="favor" v-else-if="currentPage === 'favor'">
      <div class="search">
        <input type="text" placeholder="Введите название улицы или филиала">
      </div>
      <div class="favor_card_container">
        <div class="favor_card">
          <div class="favor_compo-wrapper">
            <img src="../../static/img/barber.svg" alt="">
            <p class="favor_text">Комплексная мужская<br>стрижка</p>
          </div>
          <div class="compo-wrapper-tariff">
            <div class="tariff">
              <div class="tariff-item">
                <p class="tariff_text">3000 тнг</p>
              </div>
              <div class="dot"></div>
              <div class="tariff-item">
                <p class="tariff_text">1 час</p>
              </div>
            </div>
            <button @click="toggleSelection" v-if="!isCircleShown" class="btn-wrapper">Выбрать</button>
            <div v-else class="delete">
              <button @click="resetSelection" class="delete-btn">
                <img src="../../static/img/trash_2.svg" alt="Иконка Удаления">
              </button>
            </div>
          </div>
        </div>
  
        <div class="favor_card">
          <div class="favor_compo-wrapper">
            <img src="../../static/img/barber.svg" alt="">
            <p class="favor_text">Комплексная мужская<br>стрижка</p>
          </div>
          <div class="compo-wrapper-tariff">
            <div class="tariff">
              <div class="tariff-item">
                <p class="tariff_text">3000 тнг</p>
              </div>
              <div class="dot"></div>
              <div class="tariff-item">
                <p class="tariff_text">1 час</p>
              </div>
            </div>
            <button @click="toggleSelection" v-if="!isCircleShown" class="btn-wrapper">Выбрать</button>
            <div v-else class="delete">
              <button @click="resetSelection" class="delete-btn">
                <img src="../../static/img/trash_2.svg" alt="Иконка Удаления">
              </button>
            </div>
          </div>
        </div>
  
        <div class="favor_card">
          <div class="favor_compo-wrapper">
            <img src="../../static/img/barber.svg" alt="">
            <p class="favor_text">Комплексная мужская<br>стрижка</p>
          </div>
          <div class="compo-wrapper-tariff">
            <div class="tariff">
              <div class="tariff-item">
                <p class="tariff_text">3000 тнг</p>
              </div>
              <div class="dot"></div>
              <div class="tariff-item">
                <p class="tariff_text">1 час</p>
              </div>
            </div>
            <button @click="toggleSelection" v-if="!isCircleShown" class="btn-wrapper">Выбрать</button>
            <div v-else class="delete">
              <button @click="resetSelection" class="delete-btn">
                <img src="../../static/img/trash_2.svg" alt="Иконка Удаления">
              </button>
            </div>
          </div>
        </div>
  
        <div class="favor_card">
          <div class="favor_compo-wrapper">
            <img src="../../static/img/barber.svg" alt="">
            <p class="favor_text">Комплексная мужская<br>стрижка</p>
          </div>
          <div class="compo-wrapper-tariff">
            <div class="tariff">
              <div class="tariff-item">
                <p class="tariff_text">3000 тнг</p>
              </div>
              <div class="dot"></div>
              <div class="tariff-item">
                <p class="tariff_text">1 час</p>
              </div>
            </div>
            <button @click="toggleSelection" v-if="!isCircleShown" class="btn-wrapper">Выбрать</button>
            <div v-else class="delete">
              <button @click="resetSelection" class="delete-btn">
                <img src="../../static/img/trash_2.svg" alt="Иконка Удаления">
              </button>
            </div>
          </div>
        </div>
      </div>

      <div class="favor_bottom">
        <div class="card_next">
          <div class="card_next_container">
            <p class="card_next_text">Выбор филиала</p>
            <div class="divider_step_container">
              <div class="divider_step_one"></div>
              <div class="divider_step_two"></div>
            </div>
            <p class="card_next_subtext">Шаг 1 из 4</p>
          </div>
          <div class="card_btn_container">
            <button class="card_back_btn" @click="showChoice">Назад</button>
            <button class="card_next_btn" @click="showEmployees">Продолжить</button>
          </div>
        </div> 
      </div>

    </div>
    <div class="employees" v-else-if="currentPage === 'employees'">
      <div class="search">
        <input type="text" placeholder="Введите название улицы или филиала">
      </div>

      <div class="employees_card_container">

        <div class="employees_card">
          <div class="employees_compo-wrapper">
            <div class="user-alt">
              <img src="../../static/img/user-alt.svg" alt="">
            </div>
            <div class="employees_container">
              <p class="employees_text">Любой сотрудник</p>
              <p class="employees_subtext">Система подберет случайного специалиста</p>
            </div>

          </div>
          <div class="alt_btn">
            <button @click="toggleSelection" v-if="!isCircleShown" class="btn-wrapper">Выбрать</button> 
            <div v-else class="delete">
              <button @click="resetSelection" class="delete-btn">
                <img src="../../static/img/trash_2.svg" alt="Иконка Удаления">
              </button>
            </div>
          </div>
        </div>

        <div class="employees_card">
          <div class="employees_compo-wrapper">
            <img src="../../static/img/barber.svg" alt="">
            <div class="employees_container">
              <p class="employees_text">Юлия Дайценко</p>
              <p class="employees_subtext">Мастер SPA</p>
            </div>

          </div>
          <div class="compo-wrapper-tariff">
            <div class="employees_rate">
              <div class="star_container">
                <svg width="18" height="17" viewBox="0 0 18 17" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path fill-rule="evenodd" clip-rule="evenodd" d="M12.2575 5.95727C11.7944 5.95727 11.3874 5.66134 11.2602 5.2321L11.2426 5.1728C11.2405 5.16555 11.2382 5.15833 11.2359 5.15112L9.7288 0.469756C9.7288 0.469756 9.7288 0.469756 9.7288 0.469756C9.53202 -0.141467 8.64216 -0.1614 8.41615 0.440352C8.41615 0.440352 8.41615 0.440352 8.41615 0.440352L6.65496 5.12944C6.64683 5.15109 6.63948 5.17301 6.63292 5.19515L6.62196 5.23211C6.49474 5.66134 6.08776 5.95727 5.62468 5.95727H5.582H0.693556C0.693556 5.95727 0.693556 5.95727 0.693556 5.95727C0.0294735 5.95727 -0.253536 6.77131 0.276429 7.15708C0.276429 7.15708 0.27643 7.15708 0.276429 7.15708L4.37907 10.1434C4.39527 10.1552 4.41183 10.1666 4.42873 10.1774L4.48064 10.2108C4.85591 10.452 5.02647 10.8993 4.90256 11.3174L4.87737 11.4024C4.87568 11.4081 4.87393 11.4138 4.87213 11.4195L3.37747 16.1422C3.18269 16.7577 3.92148 17.2519 4.45137 16.8606L8.27591 14.0367C8.28719 14.0284 8.29829 14.0198 8.30921 14.011L8.33601 13.9895C8.72065 13.6805 9.27936 13.6805 9.66399 13.9895L9.6908 14.011C9.70171 14.0198 9.71282 14.0284 9.7241 14.0367L13.5486 16.8606C14.0785 17.2519 14.8173 16.7577 14.6225 16.1422L13.1279 11.4195C13.1261 11.4138 13.1243 11.4081 13.1226 11.4024L13.0974 11.3174C12.9735 10.8993 13.1441 10.452 13.5194 10.2108L13.5713 10.1774C13.5882 10.1666 13.6047 10.1552 13.6209 10.1434L17.7236 7.15708C17.7236 7.15708 17.7236 7.15708 17.7236 7.15708C18.2535 6.77131 17.9705 5.95727 17.3064 5.95727H12.3001H12.2575Z" fill="#F7D37D"/>
                </svg>
                <svg width="18" height="17" viewBox="0 0 18 17" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path fill-rule="evenodd" clip-rule="evenodd" d="M12.2575 5.95727C11.7944 5.95727 11.3874 5.66134 11.2602 5.2321L11.2426 5.1728C11.2405 5.16555 11.2382 5.15833 11.2359 5.15112L9.7288 0.469756C9.7288 0.469756 9.7288 0.469756 9.7288 0.469756C9.53202 -0.141467 8.64216 -0.1614 8.41615 0.440352C8.41615 0.440352 8.41615 0.440352 8.41615 0.440352L6.65496 5.12944C6.64683 5.15109 6.63948 5.17301 6.63292 5.19515L6.62196 5.23211C6.49474 5.66134 6.08776 5.95727 5.62468 5.95727H5.582H0.693556C0.693556 5.95727 0.693556 5.95727 0.693556 5.95727C0.0294735 5.95727 -0.253536 6.77131 0.276429 7.15708C0.276429 7.15708 0.27643 7.15708 0.276429 7.15708L4.37907 10.1434C4.39527 10.1552 4.41183 10.1666 4.42873 10.1774L4.48064 10.2108C4.85591 10.452 5.02647 10.8993 4.90256 11.3174L4.87737 11.4024C4.87568 11.4081 4.87393 11.4138 4.87213 11.4195L3.37747 16.1422C3.18269 16.7577 3.92148 17.2519 4.45137 16.8606L8.27591 14.0367C8.28719 14.0284 8.29829 14.0198 8.30921 14.011L8.33601 13.9895C8.72065 13.6805 9.27936 13.6805 9.66399 13.9895L9.6908 14.011C9.70171 14.0198 9.71282 14.0284 9.7241 14.0367L13.5486 16.8606C14.0785 17.2519 14.8173 16.7577 14.6225 16.1422L13.1279 11.4195C13.1261 11.4138 13.1243 11.4081 13.1226 11.4024L13.0974 11.3174C12.9735 10.8993 13.1441 10.452 13.5194 10.2108L13.5713 10.1774C13.5882 10.1666 13.6047 10.1552 13.6209 10.1434L17.7236 7.15708C17.7236 7.15708 17.7236 7.15708 17.7236 7.15708C18.2535 6.77131 17.9705 5.95727 17.3064 5.95727H12.3001H12.2575Z" fill="#F7D37D"/>
                </svg>
                <svg width="18" height="17" viewBox="0 0 18 17" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path fill-rule="evenodd" clip-rule="evenodd" d="M12.2575 5.95727C11.7944 5.95727 11.3874 5.66134 11.2602 5.2321L11.2426 5.1728C11.2405 5.16555 11.2382 5.15833 11.2359 5.15112L9.7288 0.469756C9.7288 0.469756 9.7288 0.469756 9.7288 0.469756C9.53202 -0.141467 8.64216 -0.1614 8.41615 0.440352C8.41615 0.440352 8.41615 0.440352 8.41615 0.440352L6.65496 5.12944C6.64683 5.15109 6.63948 5.17301 6.63292 5.19515L6.62196 5.23211C6.49474 5.66134 6.08776 5.95727 5.62468 5.95727H5.582H0.693556C0.693556 5.95727 0.693556 5.95727 0.693556 5.95727C0.0294735 5.95727 -0.253536 6.77131 0.276429 7.15708C0.276429 7.15708 0.27643 7.15708 0.276429 7.15708L4.37907 10.1434C4.39527 10.1552 4.41183 10.1666 4.42873 10.1774L4.48064 10.2108C4.85591 10.452 5.02647 10.8993 4.90256 11.3174L4.87737 11.4024C4.87568 11.4081 4.87393 11.4138 4.87213 11.4195L3.37747 16.1422C3.18269 16.7577 3.92148 17.2519 4.45137 16.8606L8.27591 14.0367C8.28719 14.0284 8.29829 14.0198 8.30921 14.011L8.33601 13.9895C8.72065 13.6805 9.27936 13.6805 9.66399 13.9895L9.6908 14.011C9.70171 14.0198 9.71282 14.0284 9.7241 14.0367L13.5486 16.8606C14.0785 17.2519 14.8173 16.7577 14.6225 16.1422L13.1279 11.4195C13.1261 11.4138 13.1243 11.4081 13.1226 11.4024L13.0974 11.3174C12.9735 10.8993 13.1441 10.452 13.5194 10.2108L13.5713 10.1774C13.5882 10.1666 13.6047 10.1552 13.6209 10.1434L17.7236 7.15708C17.7236 7.15708 17.7236 7.15708 17.7236 7.15708C18.2535 6.77131 17.9705 5.95727 17.3064 5.95727H12.3001H12.2575Z" fill="#F7D37D"/>
                </svg>
                <svg width="18" height="17" viewBox="0 0 18 17" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path fill-rule="evenodd" clip-rule="evenodd" d="M12.2575 5.95727C11.7944 5.95727 11.3874 5.66134 11.2602 5.2321L11.2426 5.1728C11.2405 5.16555 11.2382 5.15833 11.2359 5.15112L9.7288 0.469756C9.7288 0.469756 9.7288 0.469756 9.7288 0.469756C9.53202 -0.141467 8.64216 -0.1614 8.41615 0.440352C8.41615 0.440352 8.41615 0.440352 8.41615 0.440352L6.65496 5.12944C6.64683 5.15109 6.63948 5.17301 6.63292 5.19515L6.62196 5.23211C6.49474 5.66134 6.08776 5.95727 5.62468 5.95727H5.582H0.693556C0.693556 5.95727 0.693556 5.95727 0.693556 5.95727C0.0294735 5.95727 -0.253536 6.77131 0.276429 7.15708C0.276429 7.15708 0.27643 7.15708 0.276429 7.15708L4.37907 10.1434C4.39527 10.1552 4.41183 10.1666 4.42873 10.1774L4.48064 10.2108C4.85591 10.452 5.02647 10.8993 4.90256 11.3174L4.87737 11.4024C4.87568 11.4081 4.87393 11.4138 4.87213 11.4195L3.37747 16.1422C3.18269 16.7577 3.92148 17.2519 4.45137 16.8606L8.27591 14.0367C8.28719 14.0284 8.29829 14.0198 8.30921 14.011L8.33601 13.9895C8.72065 13.6805 9.27936 13.6805 9.66399 13.9895L9.6908 14.011C9.70171 14.0198 9.71282 14.0284 9.7241 14.0367L13.5486 16.8606C14.0785 17.2519 14.8173 16.7577 14.6225 16.1422L13.1279 11.4195C13.1261 11.4138 13.1243 11.4081 13.1226 11.4024L13.0974 11.3174C12.9735 10.8993 13.1441 10.452 13.5194 10.2108L13.5713 10.1774C13.5882 10.1666 13.6047 10.1552 13.6209 10.1434L17.7236 7.15708C17.7236 7.15708 17.7236 7.15708 17.7236 7.15708C18.2535 6.77131 17.9705 5.95727 17.3064 5.95727H12.3001H12.2575Z" fill="#F7D37D"/>
                </svg>
                <svg width="18" height="17" viewBox="0 0 18 17" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path fill-rule="evenodd" clip-rule="evenodd" d="M13.1279 11.4195L14.6225 16.1422C14.8173 16.7577 14.0785 17.2519 13.5486 16.8606L9.7241 14.0367C9.33946 13.7277 8.66054 13.7277 8.27591 14.0367L4.45137 16.8606C3.92148 17.2519 3.18269 16.7577 3.37747 16.1422L4.87213 11.4195C4.99604 11.0014 4.75434 10.3846 4.37907 10.1434L0.276429 7.15708C-0.253536 6.77131 0.0294735 5.95727 0.693556 5.95727H5.582C6.04508 5.95727 6.52774 5.55867 6.65496 5.12944L8.41615 0.440352C8.64216 -0.1614 9.53202 -0.141467 9.7288 0.469756L11.2426 5.1728C11.3698 5.60204 11.8371 5.95727 12.3001 5.95727H17.3064C17.9705 5.95727 18.2535 6.77131 17.7236 7.15708L13.6209 10.1434C13.2457 10.3846 13.004 11.0014 13.1279 11.4195ZM13.0512 9.32131L16.2989 6.95727H12.3001C11.398 6.95727 10.5455 6.3166 10.2878 5.47017L9.04518 1.60965L7.60128 5.45397C7.46294 5.88503 7.17789 6.24179 6.86355 6.48962C6.53959 6.74502 6.09137 6.95727 5.582 6.95727H1.70114L4.94884 9.32131C5.34504 9.58694 5.6032 9.98792 5.74502 10.3532C5.88916 10.7246 5.97464 11.2187 5.83091 11.7036L5.8283 11.7124L4.63541 15.4817L7.66859 13.2421C8.07252 12.926 8.5664 12.8049 9 12.8049C9.43362 12.8049 9.9275 12.926 10.3314 13.2421L13.3646 15.4817L12.1717 11.7124L12.1691 11.7036C12.0254 11.2187 12.1108 10.7246 12.255 10.3532C12.3968 9.9879 12.655 9.58693 13.0512 9.32131Z" fill="#AFB6C1"/>
                </svg>
              </div>
              <p class="employees_rate_text">1 отзывов</p>
            </div>
            <button @click="toggleSelection" v-if="!isCircleShown" class="btn-wrapper">Выбрать</button>
            <div v-else class="delete">
              <button @click="resetSelection" class="delete-btn">
                <img src="../../static/img/trash_2.svg" alt="Иконка Удаления">
              </button>
            </div>
          </div>
        </div>
      </div>

      <div class="employees_bottom">
        <div class="card_next">
          <div class="card_next_container">
            <p class="card_next_text">Выбор филиала</p>
            <div class="divider_step_container">
              <div class="employees_divider_step_one"></div>
              <div class="employees_divider_step_two"></div>
            </div>
            <p class="card_next_subtext">Шаг 2 из 4</p>
          </div>
          <div class="card_btn_container">
            <button class="card_back_btn" @click="showFavor">Назад</button>
            <button class="card_next_btn" @click="showEmployees">Продолжить</button>
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
      currentPage: 'branch' // Изначально показывается страница Favor
    };
  },
  methods: {
    showFavor() {
      this.currentPage = 'favor'; // Показать страницу Favor
    },
    showChoice() {
      this.currentPage = 'choice'; // Показать страницу Choice
    },
    showEmployees() {
      this.currentPage = 'employees'; // Показать страницу Choice
    }
  }
};
</script>

<style scoped>
.main{
  width: 600px;
  height: 560px;
  border-radius: 20px;
  background: #FFFFFF;
}
.choice{
  display: flex;
  flex-direction: column;
  gap: 20px;
  padding: 30px 40px;
  border-radius: 25px;
  height: 427px;
  background: #FFFFFF; 
}
.branch{
  display: flex;
  flex-direction: column;
  gap: 10px;
  padding: 30px 40px;
  border-radius: 25px;
  height: 427px;
  background: #FFFFFF;
}
.search input{
  background-color: #ffffff;
  color:#D2D8DE;
  margin: 0;
  width: 100%;
  border: 1px solid #D2D8DE;
}

.search input:focus{
  outline: none;
  border: 1px solid #6266EA;
}
.search input{
  background-image: url(../../static/img/search.svg);
  background-repeat: no-repeat;
  padding-left: 35px;
  background-position: 15px;
}
.card{
  display: flex;
  align-items: center;
  gap: 20px;
}
.card_container{
  width: 245px;
  display: flex;
  flex-direction: column;
  gap: 5px;
}
.card_address_container{
  display: flex;
  gap: 5px;
}
.card_time_container{
  display: flex;
  gap: 5px;
}
.card_name{
  font-family: TT Norms Medium;
  font-size: 16px;
  line-height: 16px;
  letter-spacing: 0em;
  text-align: left;
  color: #535C69;
  margin: 0;
}
.card_address{
  font-family: TT Norms Medium;
  font-size: 12px;
  line-height: 24px;
  letter-spacing: 0em;
  text-align: left;
  color: #AFB6C1;
  margin: 0;
}
.card_time{
  font-family: TT Norms Medium;
  font-size: 12px;
  line-height: 12px;
  letter-spacing: 0em;
  text-align: left;
  color: #AFB6C1;
  margin: 0;
}
.card_next_container{
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-top: 25px;
}
.card_next{
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.card_next_text{
  font-family: TT Norms Medium;
  font-size: 16px;
  line-height: 16px;
  letter-spacing: 0em;
  text-align: left;
  color: #535C69;
  margin: 0;
}
.divider{
  width: 201px;
  height: 3px;
  border-radius: 15px;
  background: #D8DDE3;
  margin: 0;
}
.card_next_subtext{
  font-family: TT Norms Medium;
  font-size: 10px;
  line-height: 10px;
  letter-spacing: 0em;
  text-align: left;
  color: #535C69;
  margin: 0;
}
.card_number{
  color: #6266EA;
}
.card_next_btn{
  background: #FAFAFA;
  color: #D2D8DE;
}
.choice_overview{
  display: flex;
  justify-content: space-between;
  height: 90px;
  background: #FAFAFA;
  padding: 20px;
  border-radius: 15px;
}
.choice_rate_container{
  display: flex;
  align-items: center;
  gap: 15px;
}
.choice_rate{
  font-family: TT Norms Medium;
  font-size: 42px;
  line-height: 50px;
  letter-spacing: 0em;
  text-align: center;
  color: #535C69;
}
.choice_star_text{
  font-family: TT Norms Medium;
  font-size: 10px;
  line-height: 10px;
  letter-spacing: 0em;
  text-align: left;
  color: #535C69;
  text-decoration: underline;
  cursor: pointer;
}
p{
  margin: 0;
}
.stars{
  display: flex;
  gap: 7px;
}
.choice_star_container{
  display: flex;
  flex-direction: column;
  gap: 7px;
}
.choice_info_container{
  display: flex;
  align-items: center;
  gap: 10px;
}
.choice_info_text{
  font-family: TT Norms Medium;
  font-size: 14px;
  line-height: 24px;
  letter-spacing: 0em;
  text-align: left;
  color: #535C69;
}
.service{
  display: flex;
  gap: 20px;
}
.service_container{
  padding: 20px;
  width: 250px;
  height: 170px;
  background: #F5F5F5;
  border-radius: 15px;
}
.service_container_text{
  font-family: TT Norms Medium;
  font-size: 20px;
  line-height: 24px;
  letter-spacing: 0em;
  text-align: left;
  color: #535C69;
}
.favor{
  display: flex;
  flex-direction: column;
  gap: 30px;
  padding: 30px 40px;
  height: 427px;
  background: #FFFFFF;
  border-radius: 25px;
}
.favor_card_container{
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-template-rows: repeat(2, 1fr);
  grid-column-gap: 10px;
  grid-row-gap: 10px;
}
.favor_card{
  background: #fafafa;
  border-radius: 10px;
  padding: 5px;
  width: 255px;
}
.favor_compo-wrapper{
  display: flex;
  gap: 10px;
}
.favor_text{
  text-align: left;
  font-family: TT Norms Medium;
  font-size: 14px;
  font-weight: 500;
  line-height: 17px;
  color: #535C69;  
}
.compo-wrapper-tariff{
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.tariff{
  display: flex;
  align-items: center;
  gap: 5px;
}
.tariff_text{
  font-family: TT Norms Medium;
  font-size: 12px;
  line-height: 12px;
  letter-spacing: 0em;
  text-align: left;
  color: #535C69;
}
.dot {
  display: flex;
  align-items: center;
  height: 2px;
  width: 2px;
  background: #6266EA;
  border-radius: 5px;
}
.btn-wrapper{
  border-radius: 100px;
  background: #EBEDFF;
  color: #6266EA;
  font-weight: 500;
  padding: 2px 20px;
}
.btn_wrapper:hover{
  background: #6266EA;
}
.divider_step_container{
  display: flex;
  gap: 5px;
}
.divider_step_one{
  width: 30px;
  height: 3px;
  border-radius: 100px;
  background: #6266EA;
}
.divider_step_two{
  width: 166px;
  height: 3px;
  border-radius: 100px;
  background: #D8DDE3;
}
.card_btn_container{
  display: flex;
  gap: 10px;
}
.card_back_btn{
  background: #FFFFFF;
  color: #535C69;
}
.card_back_btn:hover{
  background: #FFFFFF;
  color: #6266EA;
}
.employees{
  display: flex;
  flex-direction: column;
  gap: 30px;
  padding: 30px 40px;
  height: 427px;
  background: #FFFFFF;
  border-radius: 25px;
}
.employees_divider_step_one{
  width: 107px;
  height: 3px;
  border-radius: 100px;
  background: #6266EA;
}
.employees_divider_step_two{
  width: 91px;
  height: 3px;
  border-radius: 100px;
  background: #D8DDE3;
}
.employees_card_container{
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-template-rows: repeat(2, 1fr);
  grid-column-gap: 10px;
  grid-row-gap: 10px;
}
.employees_card{
  background: #fafafa;
  border-radius: 10px;
  padding: 5px;
  width: 255px;
}
.employees_compo-wrapper{
  display: flex;
  gap: 10px;
}
.employees_text{
  text-align: left;
  font-family: TT Norms Medium;
  font-size: 14px;
  font-weight: 500;
  line-height: 17px;
  color: #535C69;  
}
.employees_subtext{
  font-family: TT Norms Medium;
  font-size: 12px;
  line-height: 12px;
  letter-spacing: 0em;
  text-align: left;
  color: #535C69;
}
.employees_container{
  display: flex;
  flex-direction: column;
  gap: 5px;
}
.star_container{
  display: flex;
  gap: 5px;
}
.employees_rate{
  display: flex;
  flex-direction: column;
  gap: 5px;
}
.employees_rate_text{
  font-family: TT Norms Medium;
  font-size: 10px;
  line-height: 10px;
  letter-spacing: 0em;
  text-align: left;
  color: #535C69;
  text-decoration: underline;
  cursor: pointer;
}
.user-alt{
  width: 70px;
  height: 54px;
  background: #FFFFFF;
  display: flex;
  align-items: center;
  justify-content: center;
}
.alt_btn{
  display: flex;
  justify-content: end;
}
.btn-wrapper:hover{
  background: #E0E4FF;
  color: #6266EA;
}
</style>