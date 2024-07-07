<template>
  <div class="main_page">
    <div class="tariff">
      <div class="tariff_header">
        <p class="tariff_header">Ваш тариф</p>
        <p class="tariff_subheader">Бесплатный</p>
      </div>
      <div class="remain">
        <div class="remain_head">
          <p class="remain_header">Тариф продлен</p>
          <p class="remain_subheader">Осталось 364 дня</p>
        </div>
        <p class="remain_descr">Вы участвуете в бесплатном бета-тестировании сервиса, поэтому, весь функционал для вас бесплатный</p>
      </div>
      <div class="btn_container">
        <button>Продлить</button>
        <button>Новый тариф</button>
      </div>
    </div>
    <div class="tarrif_cost">
      <div class="tarrif_cost_head">
        <div class="tarrif_cost_container">
          <p class="tarrif_cost_header">Стоимость</p>
          <p class="tarrif_cost_subheader">0 ₸ /мес </p>
        </div>
        <div class="tarrif_cost_container">
          <p class="tarrif_cost_header">Срок действия</p>
          <p class="tarrif_cost_subheader">04.05.2025</p>
        </div>
        <div class="tarrif_cost_container">
          <p class="tarrif_cost_header">Способ оплаты</p>
          <p class="tarrif_cost_subheader">Не подключен</p>
        </div>
      </div>
      <button>Настроить способ оплаты</button>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
button{
  color: #6266EA;
  background: #EFEFFF;
  transition: all 0.3s ease;
}
button:hover{
  color: #FFFFFF;
  background: #6266EA;
}
p{
  margin: 0;
}
.main_page{
  background: #FFFFFF;
  display: flex;
  align-items: center;
  gap: 20px;
  width: 50%;
  padding: 20px 30px 20px 20px;
  border-radius: 5px;
}
.tariff{
  display: flex;
  flex-direction: column;
  gap: 15px;
  width: 50%;
}
.tariff_header{
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.tariff_header{
  font-family: TT Norms Medium;
  font-size: 18px;
  line-height: 21.24px;
  text-align: left;
  color: #535C69;
}
.tariff_subheader{
  font-family: TT Norms Bold;
  font-size: 36px;
  font-weight: 700;
  line-height: 36px;
  text-align: left;
  color: #535C69;
}
.remain{
  display: flex;
  flex-direction: column;
  gap: 8px;
  background: #F4FBFA;
  padding: 15px;
  border-radius: 5px;
}
.remain_head{
  display: flex;
  flex-direction: column;
  gap: 5px;
}
.remain_header{
  font-family: TT Norms Medium;
  font-size: 10px;
  line-height: 12px;
  letter-spacing: 0.05em;
  text-align: left;
  color: #0BB6A1;
}
.remain_subheader{
  font-family: TT Norms Bold;
  font-size: 21px;
  line-height: 24.78px;
  text-align: left;
  color: #0BB6A1;
}
.remain_descr{
  font-family: TT Norms Medium;
  font-size: 14px;
  line-height: 16.8px;
  text-align: left;
  color: #535C69;
}
.btn_container{
  display: flex;
  gap: 10px;
}
.tarrif_cost{
  display: flex;
  flex-direction: column;
  gap: 15px;
}
.tarrif_cost_head{
  display: flex;
  flex-direction: column;
  gap: 25px;
}
.tarrif_cost_container{
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.tarrif_cost_header{
  font-family: TT Norms Medium;
  font-size: 14px;
  line-height: 16.52px;
  text-align: left;
  color: #535C69;
}
.tarrif_cost_subheader{
  font-family: TT Norms Medium;
  font-size: 21px;
  line-height: 24.78px;
  text-align: left;
  color: #535C69;
}
</style>