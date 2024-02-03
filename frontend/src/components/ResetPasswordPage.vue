<template>
    <div class="resetpass">
      <div class="container">
        <div class="header">
          <div class="subheader">SKED</div>
          <div class="subtext">Онлайн запись — легко!</div>
        </div>
        <div class="Forma">
          <div class="resetpass-prompt">
            Нет аккаунта? <a href="#/register" class="login-link" style="text-decoration: none;">Зарегистрироваться</a>
          </div>
          <div class="resetpass-form">
            <h2>Восстановление<br>пароля</h2>
                <p class="pass_change">Пароль успешно изменен!</p>
              <div class="resetpass">
                <a href="#" style="text-decoration: none;"><button type="submit">Войти</button></a>
              </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
  export default {
    data() {
      return {
      };
    },
  };
</script>
  
  
  
    
<style>
    .pass_change{
      color:#535C69;
      font-size: 13px;
      font-style: normal;
      font-weight: 500;
      line-height: normal;
      margin-bottom: 20px;
      text-align: left;
    }
    
    .resetpass-prompt {
      padding: 0 80px 0 0;
      text-align: left;
      width: 340px;
      color: var(--cold-text-ghost-500, #DDE1E5);
      font-family: "TT Norms";
      font-size: 13px;
      font-style: normal;
      font-weight: 500;
      line-height: normal;
      margin-bottom: 10px;
    }
    
    .resetpass-link {
      color: #04C562;
      text-decoration: underline;
      cursor: pointer;
    }
    
    .resetpass-form {
      background: #fff;
      width: 340px;
      height: 250px;
      margin: 0 auto;
      padding: 40px;
      border-radius: 5px;
      box-shadow: 0px 4px 20px 0px rgba(0, 0, 0, 0.10);
    }
    </style>