<template>
  <div class="main">
    <div class="graph_container">
      <div class="graph">
        <div class="graph_header">
          <div class="graph_header_contaner">
            <div class="circle">
              <svg width="24" height="24" viewBox="0 0 16 17" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M8 2.1C4.48183 2.1 1.6 4.98183 1.6 8.5C1.6 12.0182 4.48183 14.9 8 14.9V16.5C3.59817 16.5 0 12.9018 0 8.5C0 4.09817 3.59817 0.5 8 0.5C12.4018 0.5 16 4.09817 16 8.5C16 12.7506 14 15.7 11.2 15.7C8.8 15.7 7.2 13.46 7.2 10.9H6.39998C5.51632 10.9 4.79998 10.1836 4.79998 9.29997L4.79999 6.89998H5.93488V4.66746C5.93488 4.31809 6.21808 4.03489 6.56744 4.03489C6.91679 4.03489 7.19999 4.31809 7.19999 4.66746V6.89998H8.79999V4.66746C8.79999 4.31809 9.08319 4.03489 9.43256 4.03489C9.7819 4.03489 10.0651 4.31809 10.0651 4.66746V6.89998H11.2V9.29998C11.2 10.1836 10.4836 10.9 9.59999 10.9H8.8C8.8 13.3 10 14.1 11.2 14.1C12.8 14.1 14.4 12.3854 14.4 8.5C14.4 4.98183 11.5182 2.1 8 2.1Z" fill="#F8AE55"/>
              </svg>
            </div>
            <p class="circle_text">Количество загрузок виджета</p>
          </div>
          <KebabStats @changed="option => periodWidget = option"/>
        </div>
        <div class="graph_bottom">
          <div style="display: flex; align-items: center; gap: 10px;">
            <p class="number">{{ amountWidget }}</p>
            <p class="number-sub">{{ conditionalText(periodWidget) }}</p>
          </div>
          
          <div class="bottom_container">
            <p class="bottom_procent">{{ percentWidget }}%</p>
            <div class="bottom_circle">
              <img src="../../static/img/arrow_static.svg" alt="">
            </div>
          </div>
        </div>
      </div>
      <div class="graph">
        <div class="graph_header">
          <div class="graph_header_contaner">
            <div class="circle_1">
              <img src="../../static/img/send_static.svg" alt="" class="">
            </div>
            <p class="circle_text">Количество заявок</p>
          </div>
          <KebabStats @changed="option => periodZayavki = option"/>
        </div>
        <div class="graph_bottom">
          <div style="display: flex; align-items: center; gap: 10px;">
            <p class="number">{{ amountZayavki }}</p>
            <p class="number-sub">{{ conditionalText(periodZayavki) }}</p>
          </div>
          <div class="bottom_container">
            <p class="bottom_procent">{{ percentZayavki }}%</p>
            <div class="bottom_circle_1">
              <img src="../../static/img/arrow_static.svg" alt="">
            </div>
          </div>
        </div>
      </div>
      <div class="graph">
        <div class="graph_header">
          <div class="graph_header_contaner">
            <div class="circle_2">
              <img src="../../static/img/coins_static.svg" alt="" class="">
            </div>
            <p class="circle_text">Заработано</p>
          </div>
          <KebabStats @changed="option => periodIncome = option"/>
        </div>
        <div class="graph_bottom">
          <div style="display: flex; align-items: center; gap: 10px;">
            <p class="number">{{ amountIncome }}</p>
            <p class="number-sub">{{ conditionalText(periodIncome) }}</p>
          </div>
          <div class="bottom_container">
            <p class="bottom_procent">{{ percentIncome }}%</p>
            <div class="bottom_circle_2">
              <img src="../../static/img/arrow_static.svg" alt="">
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="static">
      <div class="static_header">
        <p class="static_employ">Статистика сотрудников</p>
        <div class="static_header_container">
          <div
            :class="['static_date', { 'static_date_active': activeIndex === 'day' }]"
            @click="setActive('day')"
          >
            <p class="static_date_text">День</p>
          </div>
          <div
            :class="['static_date', { 'static_date_active': activeIndex === 'week' }]"
            @click="setActive('week')"
          >
            <p class="static_date_text">Неделя</p>
          </div>
          <div
            :class="['static_date', { 'static_date_active': activeIndex === 'month' }]"
            @click="setActive('month')"
          >
            <p class="static_date_text">Месяц</p>
          </div>
          <div
            :class="['static_date', { 'static_date_active': activeIndex === 'quarter' }]"
            @click="setActive('quarter')"
          >
            <p class="static_date_text">Квартал</p>
          </div>
          <div
            :class="['static_date', { 'static_date_active': activeIndex === 'year' }]"
            @click="setActive('year')"
          >
            <p class="static_date_text">Год</p>
          </div>
        </div>
      </div>
      <div class="divider"></div>
      <div v-if="employees_stats.length>0">
        <div class="nav">
          <p class="nav_text">Сотрудник</p>
          <p class="nav_text">Количество заявок</p>
          <p class="nav_text">Доход</p>
          <p class="nav_text">Рейтинг</p>
        </div>
        <div class="nav_people" v-for="e in employees_stats" :key="e.id">
          <p class="nav_header">{{ e.employee.firstname + ' ' + e.employee.secondname }}</p>
          <p class="nav_header">{{ e.applications_count }}</p>
          <p class="nav_header">{{ e.total_income }}</p>
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
        </div>
      </div>
      <div v-else>
        <i class="pi pi-spin pi-spinner" style="font-size: 2rem;  color: #6266EA"></i>
      </div>
  
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import KebabStats from '../components/DropdownKebabStats.vue';
export default {
  components: {KebabStats},
  data() {
    return {
      activeIndex: 'day',
      employees: [],
      employees_stats: [],

      periodWidget: 'today',
      periodZayavki: 'today',
      periodIncome: 'today',

      amountWidget: 0,
      amountZayavki: 0,
      amountIncome: 0,

      percentWidget: 0,
      percentZayavki: 0,
      percentIncome: 0,
    }
  },
  watch:{
    periodWidget(){
      this.getWidgetLoads(this.periodWidget);
    },
    periodZayavki(){
      this.getApplicationCounts(this.periodZayavki);
    },
    periodIncome(){
      this.getEarnings(this.periodIncome);
    },
  },
  methods: {
    async percentageStats(){
      try {
        const responseWidgetToday = await axios.get(`http://127.0.0.1:8000/api/widget-loads/?period=today`);
        const responseWidgetYesterday = await axios.get(`http://127.0.0.1:8000/api/widget-loads/?period=yesterday`);

        const responseZayavkiToday = await axios.get(`http://127.0.0.1:8000/api/application-counts/?period=today`);
        const responseZayavkiYesterday = await axios.get(`http://127.0.0.1:8000/api/application-counts/?period=yesterday`);

        const responseIncomeToday = await axios.get(`http://127.0.0.1:8000/api/earnings/?period=today`);
        const responseIncomeYesterday = await axios.get(`http://127.0.0.1:8000/api/earnings/?period=yesterday`);

        this.percentWidget = 
      } catch (error) {
        console.error('Ошибка при обработке статистики процентов:', error);
      }
    },

    async getWidgetLoads(period)
    {
      try 
      {
        const response = await axios.get(`http://127.0.0.1:8000/api/widget-loads/?period=${period}`);
        this.amountWidget = response.data.widgets_count;
      }      
      catch (error) 
      {
        console.error('Ошибка при получении количества загрузки виджетов:', error);
        throw error; // throw error, чтобы предоставить возможность обработки ошибки вверх по стеку вызовов
      }
    },
    async getEarnings(period)
    {
      try 
      {
        const response = await axios.get(`http://127.0.0.1:8000/api/earnings/?period=${period}`);
        this.amountIncome = response.data.total_earnings;
      }
      catch (error) 
      {
        console.error('Error fetching earnings:', error);
        throw error;
      }
    },
    async getApplicationCounts(period)
    {
      try
      {
        const response = await axios.get(`http://127.0.0.1:8000/api/application-counts/?period=${period}`);
        this.amountZayavki = response.data.applications_count;
      } 
      catch (error) 
      {
        console.error('Error fetching application counts:', error);
        throw error;  // throw error, чтобы предоставить возможность обработки ошибки вверх по стеку вызовов
      }
    },
    computedStats(){
      while (this.employees_stats.length != 0) {
        this.employees_stats.pop()
      }
      setTimeout(() => {
        for (let i = 0; i < this.employees.length; i++) {
          this.getEmployeeStats(this.employees[i].id, this.activeIndex)
        }
      }, 300);
    },
    setActive(index) {
      this.activeIndex = index;
      this.computedStats();
    },
    get_employee(){
      const user_id =  this.$store.state.registrationData.user_id;

      axios.get(`http://127.0.0.1:8000/api/get_employees/?user_id=${user_id}&project=${this.$store.state.activeProjectId}`)
        .then(response => {
          this.employees = response.data;
          this.employees.reverse();
        })
        .catch(error => {
          console.error('Error fetching employees:', error);
        });
    },
    async getEmployeeStats(employeeId, period) 
    {
      try
      {
        const response = await axios.get(`http://127.0.0.1:8000/api/get_employee_stats/?employee_id=${employeeId}&period=${period}`);
        this.employees_stats.push(response.data);
      } 
      catch (error)
      {
        console.error('Ошибка при получении статистики сотрудника:', error);
        throw error; // throw error, чтобы предоставить возможность обработки ошибки вверх по стеку вызовов
      }
    },
    conditionalText(parameter) {
      let answer;
      switch (parameter) {
        case 'today':
            answer = 'За сегодня'
            break;
        case 'yesterday':
          answer = 'За вчера'
            break;
        case '7_days':
          answer = 'За 7 дней'
            break;
        case '30_days':
          answer = 'За 30 дней'
            break;
    
        default:
            break;
      }
      return answer;
    }
  },
  mounted(){
    this.get_employee();
    this.computedStats();
  },
}
</script>

<style scoped>
.main{
  width: 80%;
  display: flex;
  flex-direction: column;
  gap: 20px;
}
.graph_container{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: 1fr;
  grid-column-gap: 15px;
}
.graph{
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  border-radius: 5px;
  border: 1px solid #F5F5F5;
  background: #FFFFFF;
  height: 227px;
  padding: 15px;
}
.graph_header{
  display: flex;
  justify-content: space-between;
}
.graph_date{
  height: 28px;
  display: flex;
  align-items: center;
  gap: 5px;
  padding: 8px;
  gap: 5px;
  border-radius: 5px;
  border: 1px solid rgba(245, 245, 245, 1);
}
.graph_date_text{
  font-family: TT Norms Medium;
  font-size: 10px;
  line-height: 10px;
  text-align: left;
}
p{
  margin: 0;
}
.circle{
  display: flex;
  align-items: center;
  justify-content: center;
  width: 48px;
  height: 48px;
  border-radius: 25px;
  background: rgba(248, 174, 85, 0.1);
}
.circle_1{
  display: flex;
  align-items: center;
  justify-content: center;
  width: 48px;
  height: 48px;
  border-radius: 25px;
  background: #62D2FF1A;
}
.circle_2{
  display: flex;
  align-items: center;
  justify-content: center;
  width: 48px;
  height: 48px;
  border-radius: 25px;
  background: #04C5621A;
}
.bottom_circle_1{
  display: flex;
  justify-content: center;
  align-items: center;
  width: 24px;
  height: 24px;
  background: #62D2FF;
  border-radius: 25px;
}
.bottom_circle_2{
  display: flex;
  justify-content: center;
  align-items: center;
  width: 24px;
  height: 24px;
  background: #04C562;
  border-radius: 25px;
}
.graph_header_contaner{
  display: flex;
  gap: 15px;
  align-items: center;
}
.circle_text{
  max-width: 140px;
  font-family: TT Norms Medium;
  font-size: 16px;
  line-height: 16px;
  text-align: left;
  color: #535C69;
}
.number{
  font-family: TT Norms Medium;
  font-size: 30px;
  line-height: 30px;
  text-align: left;
  color: #535C69;
}

.number-sub{
  font-family: TT Norms Light;
  font-size: 15px;
  line-height: 15px;
  text-align: left;
  color: #535C69;
}
.graph_bottom{
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.bottom_procent{
  font-family: TT Norms Medium;
  font-size: 13px;
  line-height: 15.34px;
  letter-spacing: -0.01em;
  text-align: left;
  color: #535C69;
}
.bottom_container{
  display: flex;
  align-items: center;
  gap: 5px;
}
.bottom_circle{
  display: flex;
  justify-content: center;
  align-items: center;
  width: 24px;
  height: 24px;
  background: #F8AE55;
  border-radius: 25px;
}
.static{
  display: flex;
  flex-direction: column;
  gap: 20px;
  background: #FFFFFF;
  border: 1px solid #F5F5F5;
  padding: 20px;
  border-radius: 5px;
}
.static_employ{
  font-family: TT Norms Medium;
  font-size: 16px;
  line-height: 18.88px;
  text-align: left;
  color: #535C69;
}
.static_header{
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.static_header_container{
  display: flex;
  background: #F3F5F6;
  padding: 3px;
  border-radius: 3px;
}
.static_date{
  background: #F3F5F6;
  padding:  10px 14px;
  border-radius: 3px;
  cursor: pointer;   
}
.static_date_active{
  background: #FFFFFF;
  padding:  10px 14px;
  border-radius: 3px;
}
.static_date_text{
  font-family: TT Norms Medium;
  font-size: 14px;
  line-height: 14px;
  text-align: left;
  color: #7D838C;
  transition: all 0.3s ease;
}
.nav{
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-template-rows: 1fr;
  gap: 30px;
  margin-bottom: 10px;
}
.nav_text{
  font-family: TT Norms Medium;
  font-size: 14px;
  line-height: 16.52px;
  text-align: left;
  color: #AFB6C1;
}
.divider {
  border-bottom: 1px solid rgba(50, 56, 74, 0.1); 
  width: auto;
  margin: 0;
}
.nav_people{
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-template-rows: 1fr;
  gap: 30px;
}
.nav_header{
  font-family: TT Norms Medium;
  font-size: 14px;
  line-height: 16.52px;
  text-align: left;
  color: #535C69;
}
.stars{
  display: flex;
  gap: 7px;
}
.static_date_text:hover{
  color: #6266EA;
}
</style>

