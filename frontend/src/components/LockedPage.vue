<template>
    <div class="lock">
        <img src="../../static/img/locked.png" alt="" class="img_locked">
        <p>Вам закрыт доступ в этот раздел :(</p>
        <p>Вероятнее всего вы заполнили не всю информацию<br>о компании (сотрудники, услуги, филиалы).<br>И обратите внимание, что необходимо создать<br> хотя бы один виджет.</p>
    </div>
</template>

<script>
export default {

}
</script>

<style>
.lock {
    text-align: center;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -150%);
    width: 400px;
    height: 100px;
  }
  
  .img_locked {
    margin-bottom: 10px;
  }
  
  .lock p {
    color: #535C69;
    font-family: "TT Norms";
    font-size: 20px;
    font-weight: 500;
    line-height: 15px;
    letter-spacing: 0em;
    text-align: center;
    margin-bottom: 10px;
  }
  
  .lock p:last-child {
    font-size: 16px;
    line-height: 16px;
    color: #AFB6C1;
  }
</style>