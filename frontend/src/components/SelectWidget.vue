<template>
  <div class="custom-select" :tabindex="tabindex" @blur="open = false">
    <div class="selected" :class="{ open: open }" @click="open = !open">
      {{ getOptionName(selected).length > 0 ? getOptionName(selected) : this.placeholderdata || options[0] }}
    </div>

    <div class="items" :class="{ selectHide: !open }">
      <div v-if="!optionsList.length > 0">Здесь пока ничего нет</div>
      <div
        v-for="option in optionsList"
        :key="getOptionKey(option)"
        @click="handleOptionClick(option)"
      >
        {{ getOptionName(option) }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    options: {
      required: true,
    },
    tabindex: {
      type: Number,
      required: false,
      default: 0,
    },
    placeholderdata: {
      type: String,
    },
  },
  data() {
    return {
      selected: {},
      open: false,
    };
  },
  computed: {
    optionsList() {
      if (Array.isArray(this.options)) {
        return this.options;
      } else if (typeof this.options === 'object') {
        return Object.keys(this.options).map(key => ({
          id: key,
          name: this.options[key]
        }));
      }
      return [];
    },
  },
  methods: {
    handleOptionClick(option) {
      this.selected = option;
      this.open = false;
      this.$emit('input', option);
    },
    getOptionKey(option) {
      return option.id || option;
    },
    getOptionName(option) {
      return option && option.name !== undefined ? option.name : option;
    },
  },
  mounted() {
    if (this.optionsList.length > 0) {
      this.$emit("input", this.selected);
    }
  },
};
</script>


<style scoped>
.custom-select {
  position: relative;
  width: 100%;
  text-align: left;
  outline: none;
  height: 24px;
  line-height: 36px;
  font-family: TT Norms light;
  font-size: 13px;
}

.selected {
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #FFFFFF;
  color: #535C69;
  font-family: TT Norms light;
  font-size: 10px;
  font-weight: 300;
  line-height: 10px;
  letter-spacing: 0em;
  text-align: left;
  color: #535C69;
  width: 45px;
  height: 24px;
  cursor: pointer;
  border-radius: 3px;
  transition: all 0.2s ease;
}
.selected:hover{
  background: #6266EA;
  color: #FFFFFF;
}

.custom-select .selected.open {
  border-radius: 3px 3px 3px 3px;
}

.custom-select .items {
  width: 50px;
  font-size: 10px;
  max-height: 170px;
  overflow-y: scroll;
  margin-top: 10px;
  color: #535C69;
  border-radius: 3px 3px 3px 3px;
  position: absolute;
  background-color: #FFFFFF;
  left: 0;
  right: 0;
  z-index: 1;
  filter: drop-shadow(0 0 10px rgb(227, 227, 227));
}

.custom-select .items div {
  color: #535C69;
  padding: 0 10px;
  cursor: pointer;
  user-select: none;
}

.custom-select .items div:hover {
  background-color: #F3F5F6;
}

.selectHide {
  display: none;
}
</style>
