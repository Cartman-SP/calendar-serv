<template>
    <div class="service_card">
        <div class="card-container">
          <div class="card-header">
            <img src="../../static/img/test.png" alt="" class="service_img">
            <div class="text-container">
              <p class="text-header">
                Стрижка
              </p>
              <p class="text-subheader">
                Название услуги
              </p>
              <p class="text-header">
                1 час 30 минут
              </p>
              <p class="text-subheader">
                Длительность
              </p>
            </div>
          </div>
          <div class="line"></div>
          <div class="card-bottom">
            <div class="text-container">
              <p class="text-header">
                Индивидуальная
              </p>
              <p class="text-subheader">
                Тип записи
              </p>
            </div>
            <div class="bottom">
              <div class="text-container">
                <p class="text-header">
                  Оплата за сеанс
                </p>
                <p class="text-subheader">
                  Формат оплаты
                </p>
              </div>
              <p class="bottom-text">5000 Р</p>
            </div>
          </div>
        </div>
      </div>
</template>

<script>
export default {

}
</script>

<style>
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
    position: absolute;
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