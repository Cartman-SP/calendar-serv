<template>
  <div class="service_card">
    <div class="card-container">
      <div class="card-header">
        <img :src="'http://127.0.0.1:8000/' + usluga.serviceCover" alt="Service Cover">
        <div class="text-container">
          <p class="text-header">{{ usluga.name }}</p> <!-- Отображаем название услуги -->
        </div>
      </div>
      <div class="line"></div>
      <div class="card-bottom">
        <div class="text-container">
          <p class="text-header">Тип записи</p>
          <p class="text-subheader">{{ usluga.type.replace('individual','Индивидуальный').replace('group','Групповой').replace('rental','Аренда') }}</p>
        </div>
        <div class="bottom">
          <div class="text-container">
            <p class="text-header">Формат оплаты</p>
            <p class="text-subheader">{{ usluga.pay_type }}</p>
          </div>
          <p class="bottom-text">{{ usluga.cost }} Р</p> <!-- Отображаем стоимость услуги -->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['usluga'] // Принимаем объект Usluga через пропс
};
</script>


<style scoped>
.text-header{
    font-family: TT Norms;
    font-size: 14px;
    font-weight: bold;
    line-height: 14px;
    letter-spacing: 0em;
    color: #535C69;
    margin: 0;
    text-align: left;
  }
  .text-subheader{
    font-family: TT Norms;
    font-size: 10px;
    font-weight: 500;
    line-height: 12px;
    letter-spacing: 0em;
    color: #AFB6C1;
    margin: 0;
    margin-bottom: 10px;
    text-align: left;
  }
  .line{
    width: 100%;
    height: 1px;
    background-color: #E4EAEF;
    margin: 20px 0;
  }
  .service_card{
    width: 310px;
    height: 230px;
    background-color: #FFF;
    top: 25%;
    left: 25%;
    transform: translate(-50%, -50%);
  }
  .card-container{
    padding: 20px;
  }
  .card-header{
    display: flex;
    gap: 10px;
  }
  img{
    width: 80px;
    height: 80px;
  }
  .bottom{
    display: flex;
    justify-content: space-between;
  }
  .bottom-text{
    margin: 0;
    background-color:#EFEFFF;
    width: 95px;
    height: 34px;
    font-family: TT Norms;
    font-size: 14px;
    font-weight: bold;
    line-height: 24px;
    letter-spacing: 0em;
    color: #535C69;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 3px;
  }
</style>