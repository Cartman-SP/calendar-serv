<template>
    <div class="event" :style="{ borderColor: color }">
        <p class="event-name">Стрижка</p>
        <p class="event-time">7:30</p>
    </div>
</template>

<script>
export default {
    props:['color', 'eventData'],
}
</script>

<style scoped>

.event{
  margin: 5px;
  padding: 10px;
  border: solid 1px #FFCF7D;
  border-radius: 5px;
  width: 100%;
  background-color: white;
  transition: all .2s ease;
  cursor: pointer;
}

.event:hover{
    filter: drop-shadow(0 0 10px rgb(233, 233, 233));
}

.event-name, .event-time{
  font-family: TT Norms Medium;
  font-size: 14px;
  line-height: 16px;
  text-align: left;
  margin: 0;
  color: #535C69;
}
</style>