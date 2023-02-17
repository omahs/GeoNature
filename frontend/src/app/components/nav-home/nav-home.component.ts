
import { Component, OnInit, ViewChild, Inject } from '@angular/core';
import { MatSidenav } from '@angular/material/sidenav';

import { AuthService, User } from '../../components/auth/auth.service';
import { AppConfig } from '../../../conf/app.config';
import { GlobalSubService } from '../../services/global-sub.service';
import { SideNavService } from '../sidenav-items/sidenav-service';
import { LocaleService } from '../../services/locale.service';

@Component({
  selector: 'pnx-nav-home',
  templateUrl: './nav-home.component.html',
  styleUrls: ['./nav-home.component.scss']
})
export class NavHomeComponent implements OnInit {
  public moduleName = 'Accueil';
  public currentUser: User;
  public appConfig: any;
  public currentDocUrl: string;
  public locale: string;
  @ViewChild('sidenav') public sidenav: MatSidenav;

  constructor(
    public authService: AuthService,
    public sideNavService: SideNavService,
    private globalSubService: GlobalSubService,
    private localeService: LocaleService
  ) {}

  ngOnInit() {
    // Inject App config to use in the template
    this.appConfig = AppConfig;

    // Subscribe to router event
    this.loadLocale();

    // Set the current module name in the navbar
    this.onModuleChange();

    // Init the sidenav instance in sidebar service
    this.sideNavService.setSideNav(this.sidenav);

    // Put the user name in navbar
    this.currentUser = this.authService.getCurrentUser();
  }

  private loadLocale() {
    this.locale = this.localeService.currentLocale;
  }

  changeLanguage(lang) {
    this.localeService.setLocale(lang);
    this.locale = lang;
  }

  private onModuleChange() {
    this.globalSubService.currentModuleSub.subscribe(module => {
      if (module) {
        this.moduleName = module.module_label;
        if (module.module_doc_url) {
          this.currentDocUrl = module.module_doc_url;
        }
      } else {
        this.moduleName = 'Accueil';
      }
    });
  }

  closeSideBar() {
    this.sideNavService.sidenav.toggle();
  }
}
