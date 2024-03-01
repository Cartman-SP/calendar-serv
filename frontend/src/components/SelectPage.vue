<template>
  <div class="custom-select" :tabindex="tabindex" @blur="open = false">
    <div class="selected" :class="{ open: open }" :style="{ color: (getOptionName(selected).length > 0) ? '#535C69' : '#D2D8DE' }" @click="open = !open">
      {{ getOptionName(selected).length > 0 ? getOptionName(selected) : this.placeholderdata || options[0] }}
    </div>

    <div class="items" :class="{ selectHide: !open }">
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
  height: 36px;
  line-height: 36px;
  font-family: TT Norms Medium;
  font-size: 12px;
}

.selected {
  background-color: #F3F5F6;
  border-radius: 3px;
  padding-left: 1em;
  cursor: pointer;
  user-select: none;
  height: 36px;
}

.custom-select .selected.open {
  border-radius: 3px 3px 3px 3px;
}

.custom-select .selected:after {
  position: absolute;
  content: "";
  top: 16px;
  right: 1em;
  width: 0;
  height: 0;
  border: 3px solid transparent;
  border-color: #535C69 transparent transparent transparent;
}

.custom-select .items {
  max-height: 200px;
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
  padding-left: 1em;
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
