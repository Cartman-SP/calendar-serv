<template>
  <div class="main">
    <div class="graph_container">
      <div class="graph"></div>
      <div class="graph"></div>
      <div class="graph"></div>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.main{
  width: 60%;
}
.graph_container{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: 1fr;
  grid-column-gap: 15px;
}
.graph{
  border-radius: 5px;
  border: 1px solid #F5F5F5;
  width: 310px;
  height: 227px;
}
</style>

