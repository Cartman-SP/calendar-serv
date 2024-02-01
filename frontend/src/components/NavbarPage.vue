<template>
    <div class="nav">
        <div class="search">
            <input type="text" placeholder="Найти">
        </div>
        <div class="actions">
            <div class="buttons-menu">
                <a href="">
                    <img src="../../static/img/icon-file.png" alt="1">
                </a>
                <a href="">
                    <img src="../../static/img/icon-plus.png" alt="2">
                </a>
                <a href="">
                    <img src="../../static/img/icon-ring.png" alt="3">
                </a>
                <a href="">
                    <img src="../../static/img/icon-bell.png" alt="4">
                </a>
            </div>
            <div class="rate">
                <img src="../../static/img/icon-wallet.png" alt="231">
                <div class="text">
                    <p>Тариф</p>
                    <h4>Пробный</h4>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

</script>

<style scoped>
img{
    width: 20px;
}
.nav{
    margin: 30px 30px 30px 0px;
    height: 4vw;
    width: 100%;
    display: flex;
    background-color: #F3F6F8;
    align-items: center;
    justify-content: space-between;
    padding: 20px;
    border-radius: 10px;
}

.search input{
    background-color: #ffffff;
    color:#D2D8DE;
    margin: 0;
}

.search input:focus{
    outline: solid 1px #6266EA;
}

.actions, .buttons-menu, .rate{
    display: flex;
    align-items: center;
}

.buttons-menu a{
    background-color: white;
    width: 40px;
    height: 40px;
    border-radius: 20px;
    margin: 0 10px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.rate{
    text-align: left;
    background-color: white;
    height: 50px;
    padding: 20px;
    border-radius: 25px;
}

.text{
    margin-left: 20px;
}

.rate p{
    margin: 0;
    color: #D2D8DE;
}

.rate h4{
    margin: 0;
    color: #464AD9;
}
</style>