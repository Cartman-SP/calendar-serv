<template>
    <header>
        <div class="buttons">
            <a href="#/login"><button class="enter">Вход</button></a>
            <a href="#/register"><button class="register">Регистрация</button></a>
        </div>
    </header>
</template>

<script>
export default {

}
</script>

<style>
body{
    background: url('static/viewapp/img/bg.svg') no-repeat center center fixed;
    background-size: cover;
}

.buttons {
    display: flex;
    width: 100vw;
    height: 100vh;
    align-items: center;
    justify-content: center;
    gap: 50px;
  }

.buttons a{
    text-decoration: none;
    transition: .2s ease;
}

.buttons a:hover{
    filter: brightness(90%);
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
    font-family: TT Norms Medium;
    font-size: 22px;
    font-style: normal;
    font-weight: 500;
    line-height: normal;
    border-radius: 3px;
    border: 1px solid var(--cold-text-ghost-500, #DDE1E5);
    background: var(--Neutral-White, #FFF);
  }
  .enter:hover{
    color: #6266EA;
    background: #FFFFFF;
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
    font-family: TT Norms Medium;
    font-size: 22px;
    font-style: normal;
    font-weight: 500;
    line-height: normal;
    border-radius: 3px;
    background: var(---, #464AD9);
   }
  .register:hover{
    color: #6266EA;
    background: #FFFFFF;
  }
  @media (max-width: 576px){
    .buttons {
      flex-direction: column;
    }
  }
</style>