<template>
  <div id="event-icon-container" class="nav-item-container hide-mobile">
    <nav>
      <span>EVENTS</span>
      <img src="@/assets/images/event_icons.svg" alt="Menu" class="menu-icon" />
    </nav>
    <b-popover
      custom-class="event-popover"
      target="event-icon-container"
      placement="bottom"
      triggers="click"
      :show.sync="showEvents"
    >
      <!-- Shows List of Events  -->
      <EventCard />
    </b-popover>
  </div>
</template>

<script>
import EventCard from '@/components/EventCard.vue'

export default {
  components: {
    EventCard
  },
  data() {
    return {
      showEvents: false
    }
  },
  mounted() {
    this.$root.$on('closeEventPopover', e => {
      this.showEvents = false
    })
  }
}
</script>

<style lang="scss" scoped>
#event-icon-container {
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: white;
  padding: 0.5em;
  border-radius: 1.5em;
  z-index: 50;
  margin-right: 0.5em;
  box-shadow: 0px 3px 6px #00000022;
  border: 1px solid #beb2a5;
  color: #151515;
  font-weight: 800;
  font-size: 12px;

  .menu-icon {
    width: 15px;
    height: 15px;
  }

  .arts-container & {
    margin: 0 0.25em;
    width: 45px;
    height: 45px;
  }

  .arts-container & > span {
    display: none;
  }

  .arts-container & > .menu-icon {
    margin: 0;
  }

  @media (max-width: 1350px) {
    & {
      width: 45px;
      height: 45px;
      margin: 0 0.25em;
    }
    span {
      display: none;
    }
  }
}

.notify-badge {
  position: absolute;
  top: 2.5px;
  right: 5px;
  width: 10px;
  height: 10px;
  background-color: rgba(173, 20, 20, 0.753);
  border-radius: 50%;
}

.popover {
  width: 425px !important;
  max-width: 425px !important;
  height: auto;
  max-height: 650px;
  overflow-y: hidden;
}

.event-popover .popover-body {
  padding: 0 !important;
}
</style>
