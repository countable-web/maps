<template>
  <div ref="sidebarContainer" class="ds">
    <div class="ds-container" :style="'width: ' + width + 'px;'">
      <Logo :logo-alt="2" class="pt-2 pb-2"></Logo>

      <slot name="header"></slot>
      <slot name="badges"></slot>
      <slot name="content"></slot>
      <slot></slot>
      <Contact
        :subject="
          `FPCC Map: Didn't find what I was looking for (${$route.path})`
        "
      ></Contact>
    </div>
    <div class="detail-sidebar-mobile sidebar-mobile d-none cursor-pointer">
      <SideBarFold>
        <template v-slot:badges>
          <slot name="badges"></slot>
        </template>
        <slot name="content"></slot>
        <slot></slot>
      </SideBarFold>
    </div>
  </div>
</template>

<script>
import Contact from '@/components/Contact.vue'
import Logo from '@/components/Logo.vue'
import SideBarFold from '@/components/SideBarFold.vue'

export default {
  components: {
    Contact,
    Logo,
    SideBarFold
  },
  props: {
    width: {
      default: 375,
      type: Number
    }
  },
  data() {
    return {
      style: 2
    }
  }
}
</script>

<style>
.ds-container {
  position: fixed;
  top: 0;
  left: 0;
  bottom: 0;
  width: var(--sidebar-width, 350px);
  background-color: white;
  overflow-y: auto;
  padding-bottom: 1em;
}

.ds-container .badge-container {
  padding: 0 1em;
  padding-top: 1em;
}

.ds-container .badge {
  margin-top: 0.5em;
}

@media (max-width: 992px) {
  .ds-container {
    display: none;
  }

  .detail-sidebar-mobile {
    display: block !important;
  }

  .ds {
    width: 100%;
    top: unset;
    padding: 0;
    margin: 0;
    z-index: 50;
    max-height: 80%;
    bottom: 0;
    left: 0;
    position: fixed;
  }
}
</style>
