<template>
    <div class="recovery">
      <div class="container">
        <div class="header">
          <div class="subheader">SKED</div>
          <div class="subtext">Онлайн запись — легко!</div>
        </div>
        <div class="Forma">
          <div class="recovery-prompt">
            Нет аккаунта? <a class="recovery-link" href="#/login" style="text-decoration:none">Зарегистрироваться</a>
          </div>
          <div class="recovery-form">
            <h2>Восстановление<br>пароля</h2>
            <p class="pass_change">Мы отправили код подтверждения<br>на указанную почту</p>
            <form>
              <div class="form-group">
                <label for="username">Код подтверждения</label>
                <input type="email" id="username" name="username" placeholder="Введите код подтверждения" required>
              </div>
              <div class="form-group">
                <label for="password">Новый пароль</label>
                <div class="card flex justify-content-center">
                  <PasswordComponent v-model="passwordValue" toggleMask />
                </div>
              </div>
              <button type="submit">Сменить пароль</button>
            </form>
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

    .Forma {
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    
    .recovery-prompt {
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
    
    .recovery-link {
      color: #04C562;
      text-decoration: underline;
      cursor: pointer;
    }

    .recovery-form {
      background: #fff;
      width: 340px;
      height: 475px;
      margin: 0 auto;
      padding: 40px;
      border-radius: 5px;
      box-shadow: 0px 4px 20px 0px rgba(0, 0, 0, 0.10);
    }
    </style>