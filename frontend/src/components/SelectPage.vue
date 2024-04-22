<template>
  <div class="custom-select" tabindex="1" @blur="open = false">
    <div class="selected" :class="{ open: open }" :style="{ color: (getOptionName(selected).length > 0) ? '#535C69' : '#D2D8DE' }" @click="open = !open">
      {{ getOptionName(selected).length > 0 ? getOptionName(selected) : this.placeholderdata || options[0] }}
    </div>

    <div :class="{ selectHide: !open, items: open }">
      <div class="search" v-if="searchable" @click="open = true">
        <input type="search" placeholder="Поиск" v-model="searchTerm">
      </div>
      <div v-if="!filteredOptions.length > 0">Здесь пока ничего нет</div>
      <div
        v-for="option in filteredOptions"
        :key="getOptionKey(option)"
        @click="handleOptionClick(option)"
        style="display: flex; align-items: center;"
      >
        <span v-html="highlightMatch(getOptionName(option))"></span>
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
    placeholderdata: {
      type: String,
    },
    value: {
      default: null,
      required: false,
    },
    searchable:{
      type: Boolean,
    }
  },
  data() {
    return {
      selected: this.value || {},
      open: false,
      searchTerm: '',
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
    filteredOptions() {
      const term = this.searchTerm.toLowerCase();
      return this.optionsList.filter(option => this.getOptionName(option).toLowerCase().includes(term));
    }
  },
  watch: {
    value(newValue) {
      this.selected = newValue;
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
    highlightMatch(optionName) {
      const term = this.searchTerm.toLowerCase();
      const index = optionName.toLowerCase().indexOf(term);
      if (index > -1) {
        const highlightedPart = '<span style="color: #6266EA;">' + optionName.substr(index, term.length) + '</span>';
        return optionName.substr(0, index) + highlightedPart + optionName.substr(index + term.length);
      }
      return optionName;
    }
  },
  mounted() {
    if (this.optionsList.length > 0) {
      this.$emit("input", this.selected);
    }
  },
};
</script>





<style scoped>
.search input{
  background-image: url(../../static/img/search.svg);
  background-repeat: no-repeat;
  padding-left: 20px;
  background-position: 0;
}

.search input:focus{
    outline: none;
    border: none;
}
.search{
  background-color: white;
  border-bottom: solid 1px #C6CBD2;
}

.search input{
  margin: 0;
  color: #535C69;
  background-color: white;
}

.custom-select {
  position: relative;
  width: 100%;
  text-align: left;
  outline: none;
  height: 36px;
  line-height: 36px;
  font-family: TT Norms Medium;
  font-size: 13px;
}

.selected {
  background-color: #F3F5F6;
  border-radius: 3px;
  padding-left: .8em;
  cursor: pointer;
  user-select: none;
  height: 36px;
}

.selected.open {
  border-radius: 3px 3px 3px 3px;
}

.selected:after {
  position: absolute;
  content: "";
  top: 16px;
  right: 1em;
  width: 0;
  height: 0;
  border: 3px solid transparent;
  border-color: #535C69 transparent transparent transparent;
}

.items {
  opacity: 1;
  max-height: 170px;
  overflow: hidden;
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
  transform: translateY(0);
  transition: all .2s ease;
}

.items div {
  color: #535C69;
  padding-left: 1em;
  padding-right: .8em;
  cursor: pointer;
  user-select: none;
}

.items div:hover {
  background-color: #F3F5F6;
}

.items .search:hover {
  background-color: white;
}


.selectHide div{
  padding-left: 1em;
  padding-right: 1em;
}

.selectHide {
  opacity: 0;
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
  transform: translateY(5px);
  transition: all .2s ease;
  visibility: hidden;
}
</style>
