<template>
    <div class="lock">
        <div class="content">
            <img src="../../static/img/404.svg" alt="" class="img_locked">
            <p>К сожалению, такой страницы у нас нет :(</p>
            <p>Вероятнее всего вы перешли по неправильной или недействительной ссылке либо искомый вами раздел был удален.</p>
        </div>
        <router-link :to="'/dashboard'" style="text-decoration: none;">
            <button>На главную</button>
        </router-link>
    </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.content{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 10px;
}
.lock {
  height: 100vh;
  width: 100vw;
  text-align: center;
  align-items: center;
  justify-content: center;
  display: flex;
  flex-direction: column;
  gap: 20px;
  }
  
  .lock p {
    color: #ffffff;
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
    color: #8f959e;
  }
  p{
    margin: 0;
    max-width: 400px;
  }
</style>