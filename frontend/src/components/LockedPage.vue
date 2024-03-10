<template>
    <div class="lock">
        <img src="../../static/img/locked.svg" alt="" class="img_locked">
        <p>Вам закрыт доступ в этот раздел :(</p>
        <p>Вероятнее всего вы заполнили не всю информацию о компании (сотрудники, услуги, филиалы). И обратите внимание, что необходимо создать хотя бы один виджет.</p>
    </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.lock {
  height: 87vh;
  text-align: center;
  align-items: center;
  justify-content: center;
  display: flex;
  flex-direction: column;
  gap: 20px;
  }
  
  .lock p {
    color: #535C69;
    font-family: "TT Norms Medium";
    font-size: 20px;
    font-weight: 500;
    line-height: 15px;
    letter-spacing: 0em;
    text-align: center;
  }
  
  .lock p:last-child {
    font-size: 16px;
    line-height: 16px;
    color: #AFB6C1;
  }
  p{
    margin: 0;
    max-width: 400px;
  }
</style>