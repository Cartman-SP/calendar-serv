<template>
  <div class="main">
    <div class="head">
      Заявки
    </div>

    <div class="nav">
      <div class="nav_left">
        <SelectPage
        :options="['Пушкинский', 'Новый', 'Я люблю пельмени', 'Тест']"
        :searchable="true"
        :placeholderdata="'Выбрать филиал'"
        @input="option => selectedBranch = option"
        />
    
        <SelectPage
        :options="['Кологривый','РЫНДЫЧ','влади дади','Шишадмин' ]"
        :placeholderdata="'Выбрать Сотрудника'"
        :searchable="true"
        @input="option => selectedEmployee = option"
        />
      </div>

      <div class="nav_center">
        <div class="nav_btn_container">
          <button :class="{'request_btn' : timeRange === 'week', 'request_btn_unactive' : timeRange === 'month'}" @click="timeRange = 'week'">Неделя</button>
          <button :class="{'request_btn' : timeRange === 'month', 'request_btn_unactive' : timeRange === 'week'}" @click="timeRange = 'month'">Месяц</button>
        </div>
        <input type="date" style="width:160px">
      </div>

      <div class="search">
        <input type="text" placeholder="Поиск по заявкам">
      </div>
    </div>

    <div class="subnav">
      <div class="subnav_left_container">
        <div class="container" @click="changeTab('all')" :class="{ active: activeTab === 'all' }">
          <p class="nav_text">Все</p>
          <p class="nav_subtext">{{ allRequests }}</p>
        </div>
        <div class="container" @click="changeTab('new')" :class="{ active: activeTab === 'new' }">
          <div class="circle_accepted"></div>
          <p class="nav_text">Новые</p>
          <p class="nav_subtext">{{ newRequests }}</p>
        </div>
        <div class="container" @click="changeTab('accepted')" :class="{ active: activeTab === 'accepted' }">
          <div class="circle_taken"></div>
          <p class="nav_text">Принят</p>
          <p class="nav_subtext">{{ acceptedRequests }}</p>
        </div>
        <div class="container" @click="changeTab('completed')" :class="{ active: activeTab === 'completed' }">
          <div class="circle_completed"></div>
          <p class="nav_text">Завершен</p>
          <p class="nav_subtext">{{ finishedRequests }}</p>
        </div>
        <div class="container" @click="changeTab('canceled')" :class="{ active: activeTab === 'canceled' }">
          <div class="circle_cancelation"></div>
          <p class="nav_text">Отмен</p>
          <p class="nav_subtext">{{ canceledRequests }}</p>
        </div>
      </div>

      <div style="display: flex; align-items: center; gap: 20px;">
        <div class="subnav_page">
          <img src="../../static/img/arrow-left.svg" alt="<">
          <div class="pages">
            <div class="number">
              <p class="page_text">1</p>
              <p class="page_text">2</p>
              <p class="page_text">3</p>
            </div>
            <p class="page_text">...</p>
            <div class="number">
              <p class="page_text">56</p>
              <p class="page_text">57</p>
              <p class="page_text">58</p>
            </div>
          </div>
          <img src="../../static/img/arrow-right.svg" alt=">">
        </div>

        <div class="xls" id="excel_download" >
          <img src="../../static/img/download.svg" alt="downloadArrow">
          <p class="xls_text">XLS</p>
        </div>
      </div>
    </div>

    <div class="primary">
      <div class="primary_nav">
        <div class="status">
          <div class="mark" v-if="!Mark" @click="Mark = true"></div>
          <div class="mark_active" v-else @click="Mark = false">
            <img src="../../static/img/checkmark.svg" alt="">
          </div>
          <p class="primary_nav_text">Статус</p>
        </div>
        <p class="primary_nav_text">Дата</p>
        <p class="primary_nav_text">Клиент</p>
        <p class="primary_nav_text">Заказ</p>
        <p class="primary_nav_text">Действия</p>
      </div>
      <div class="divider"></div>
      <p class="primary_new">Выберите филиал и сотрудника,<br>чтобы посмотреть список заявок</p>
      <img src="../../static/img/request.svg" alt="" draggable="false">
      <CardRequest></CardRequest>
    </div>



  </div>
</template>

<script>
import SelectPage from '../components/SelectPage.vue';
import CardRequest from '../components/CardRequest.vue';

export default {
  components: { SelectPage, CardRequest },
  data() {
    return {
      Mark: false,
      activeTab: 'all',
      timeRange: 'week',

      allRequests: 'NaN123123123',
      newRequests: 'NaN',
      acceptedRequests: 'NaN',
      finishedRequests: 'NaN',
      canceledRequests: 'NaN',
    };
  },
  methods: {
    changeTab(tab) {
      this.activeTab = tab;
      // Здесь вы можете добавить логику для обновления содержимого компонента в соответствии с выбранной вкладкой
    }
  },
  mounted() {
    // При загрузке страницы добавляем класс active к контейнеру с текстом "Все 432"
    document.querySelector('.container').classList.add('active');
    document.querySelector('.page_text:first-child').classList.add('active');
  }
}
</script>

<style scoped>
.main{
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.head{
  font-family: TT Norms Medium;
  font-size: 20px;
  font-weight: 500;
  line-height: 23.6px;
  text-align: left;
  color: #535C69;
}
.nav{
  display: flex;
  justify-content: start;
  gap: 40px;
  margin-bottom: 20px;
}
.nav_left{
  width: 375px;
  display: flex;
  gap: 5px;
}
.nav_btn_container{
  display: flex;
  background: #F3F5F6;
  height: 36px;
  border-radius: 3px;
  padding: 3px;
}

.nav_btn_container button:hover{
  color: #6266EA;
}
.request_btn{
  padding: 10px 14px 10px 14px;
  gap: 5px;
  border-radius: 3px;
  background: #FFFFFF;
  color: #535C69;
  height: 30px;
}
.request_btn_unactive{
  padding: 10px 14px 10px 14px;
  gap: 5px;
  border-radius: 3px;
  background: #F3F5F6;
  color: #AFB6C1;
  height: 30px;

}
.nav_center{
  display: flex;
  gap: 5px;
}
.search input{
  background-color: #F3F5F6;
  color:#D2D8DE;
  margin: 0;
  width: 100%;
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
.subnav{
  width: 70%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-bottom: 10px;
  gap: 105px;
  margin-bottom: 25px;
}
.subnav_left_container{
  display: flex;
  gap: 20px;
}
.nav_text{
  color: #535C69;
  font-family: TT Norms Medium;
  font-size: 14px;
  line-height: 16.52px;
  text-align: left;
}
.nav_subtext{
  font-family: TT Norms Bold;
  font-size: 13px;
  line-height: 15.34px;
  text-align: left;
  color: #B7C0C8;
}
p {
  margin: 0;
}
.container{
  display: flex;
  align-items: center;
  gap: 5px;
  cursor: pointer;
}
.circle_accepted{
  width: 8px;
  height: 8px;
  background: #28CCF0;
  border-radius: 20px;
}
.circle_cancelation{
  width: 8px;
  height: 8px;
  background: #F97F7F;
  border-radius: 20px;
}
.circle_completed{
  width: 8px;
  height: 8px;
  background: #00A490;
  border-radius: 20px;
}
.circle_cancelation{
  width: 8px;
  height: 8px;
  background: #F97F7F;
  border-radius: 20px;
}
.circle_taken{
  width: 8px;
  height: 8px;
  background: #F7D37D;
  border-radius: 20px;
}
.container {
  position: relative;
}

.nav_text::after {
  content: '';
  position: absolute;
  left: 0;
  bottom: -10px;
  width: 100%;
  height: 2px;
  background-color: transparent;
  transition: background-color 0.3s ease;
}

.container:hover .nav_text::after {
  background-color: #4C5D6E33;
}
.container.active .nav_text::after {
  background-color: #4C5D6E33;
}
.subnav_page{
  display: flex;
  gap: 20px;
}
.number{
  display: flex;
  gap: 10px;
}
.pages{
  display: flex;
  gap: 15px;
  align-items: end;
}
.page_text{
  font-family: TT Norms Medium;
  font-size: 14px;
  line-height: 16.52px;
  text-align: center;
  color: #B7C0C8;
  cursor: pointer;
}
.page_text:hover{
  color: #6266EA;
}
.page_text.active {
  color: #6266EA;
}
.xls{
  width: 74px;
  height: 36px;
  border-radius: 3px;
  border: 1px solid #DDE1E5;
  display: flex;
  gap: 5px;
  align-items: center;
  justify-content: center;
  transition: all .2s ease;
}

.xls:hover{
  background-color: #F3F5F6;
  cursor: pointer;
}

.xls:hover .xls_text{
  color: #00A490;
}
.xls_text{
  font-family: TT Norms Medium;
  font-size: 14px;
  line-height: 16.52px;
  text-align: center;
  color: #535C69;
  transition: all .2s ease;
}
.primary{
  width: 70%;
  min-height: 468px;
  height: fit-content;
  gap: 10px;
  border-radius: 5px;
  background: #FFFFFF;
  padding: 30px 20px;
}
.primary_nav_text{
  font-family: TT Norms Medium;
  font-size: 14px;
  line-height: 16.52px;
  text-align: left;
  color: #7D838C;
}
.primary_nav{
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  grid-template-rows: 1fr;
}
.mark{
  width: 16px;
  height: 16px;
  border-radius: 3px;
  border: 1px solid #C6CBD2;
  cursor: pointer;
  user-select:none;
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
  background: var(--color-global);
  user-select:none;
}
.status{
  display: flex;
  gap: 20px;
}
.divider {
  border-bottom: 1px solid rgba(50, 56, 74, 0.1); 
  width: auto;
  margin: 10px 0;
  margin-bottom: 65px;
}
.primary_new{
  font-family: TT Norms Medium;
  font-size: 18px;
  line-height: 21.24px;
  text-align: center;
  color: #535C69;
  margin-bottom: 20px;
}
</style>
