<template>
    <header>
        <img class="background" src="../../img/Back.png" alt="">
        <div class="buttons">
          <button class="enter">Вход</button>
          <button class="register">Регистрация</button>
        </div>
    </header>
</template>

<script>
export default {

}
</script>

<style>
.buttons {
    position: absolute;
    top: 50%;
    left: 50%; 
    transform: translate(-50%, -50%);
    display: flex;
    flex-direction: row;
  }
  
  .enter{
    width: 233px;
    height: 66px;
    display: flex;
    padding: 20px 90px;
    justify-content: center;
    align-items: center;
    gap: 5px;
    color: var(--cold-text-title-200, #535C69);
    text-align: center;
    font-family: "TT Norms";
    font-size: 22px;
    font-style: normal;
    font-weight: 500;
    line-height: normal;
    border-radius: 3px;
    border: 1px solid var(--cold-text-ghost-500, #DDE1E5);
    background: var(--Neutral-White, #FFF);
  }
  
  .register{
    width: 233px;
    height: 66px;
    display: flex;
    padding: 20px 50px;
    justify-content: center;
    align-items: center;
    gap: 5px;
    color: #FFF;
    text-align: center;
    font-family: "TT Norms";
    font-size: 22px;
    font-style: normal;
    font-weight: 500;
    line-height: normal;
    border-radius: 3px;
    background: var(---, #464AD9);
    border: 1px solid var(--cold-text-ghost-500, #464AD9);
    margin-left: 50px;
   }
</style>