<?php

//CONFIGURATION for SmartAdmin UI

//ribbon breadcrumbs config
//array("Display Name" => "URL");
$breadcrumbs = array(
	"Home" => APP_URL
);

/*navigation array config

ex:
"dashboard" => array(
	"title" => "Display Title",
	"url" => "http://yoururl.com",
	"icon" => "fa-home"
	"label_htm" => "<span>Add your custom label/badge html here</span>",
	"sub" => array() //contains array of sub items with the same format as the parent
)

*/
$page_nav = array(
	"dashboard" => array(
		"title" => "Dashboard",
		"url" => "ajax/dashboard.php",
		"icon" => "fa-home"
	),
	"inbox" => array(
		"title" => "Inbox",
		"url" => "ajax/inbox.php",
		"icon" => "fa-inbox",
		"label_htm" => '<span class="badge pull-right inbox-badge">14</span>'
	),
	"graphs" => array(
		"title" => "Graphs",
		"icon" => "fa-bar-chart-o",
		"sub" => array(
			"flot" => array(
				"title" => "Flot Chart",
				"url" => "ajax/flot.php"
			),
			"morris" => array(
				"title" => "Morris Charts",
				"url" => "ajax/morris.php"
			),
			"inline" => array(
				"title" => "Inline Charts",
				"url" => "ajax/inline-charts.php"
			)
		)
	),
	"tables" => array(
		"title" => "Tables",
		"icon" => "fa-table",
		"sub" => array(
			"normal" => array(
				"title" => "Normal Tables",
				"url" => "ajax/table.php"
			),
			"data" => array(
				"title" => "Data Tables",
				"url" => "ajax/datatables.php"
			)
		)
	),
	"forms" => array(
		"title" => "Forms",
		"icon" => "fa-pencil-square-o",
		"sub" => array(
			"smart_elements" => array(
				"title" => "Smart Form Elements",
				"url" => "ajax/form-elements.php"
			),
            "smart_layout" => array(
				"title" => "Smart Form Layouts",
				"url" => "ajax/form-templates.php"
			),
            "smart_validation" => array(
				"title" => "Smart Form Validation",
				"url" => "ajax/validation.php"
			),
            "bootstrap_forms" => array(
				"title" => "Bootstrap Form Elements",
				"url" => "ajax/bootstrap-forms.php"
			),
            "form_plugins" => array(
				"title" => "Form Plugins",
				"url" => "ajax/plugins.php"
			),
            "wizards" => array(
				"title" => "Wizards",
				"url" => "ajax/wizard.php"
			),
            "bootstrap_editors" => array(
				"title" => "Bootstrap Editors",
				"url" => "ajax/other-editors.php"
			),
            "dropzone" => array(
				"title" => "Dropzone",
				"url" => "ajax/dropzone.php",
                "label_htm" => '<span class="badge pull-right inbox-badge bg-color-yellow">new</span>'
			)
		)
	),
    "ui_elements" => array(
        "title" => "UI Elements",
        "icon" => "fa-desktop",
        "sub" => array(
            "general" => array(
                "title" => "General Elements",
                "url" => "ajax/general-elements.php"
            ),
            "buttons" => array(
                "title" => "Buttons",
                "url" => "ajax/buttons.php"
            ),
            "icons" => array(
                "title" => "Icons",
                "sub" => array(
                    "fa" => array(
                        "title" => "Font Awesome",
                        "icon" => "fa-plane",
                        "url" => "fa.php"
                    ),
                    "glyph" => array(
                        "title" => "Glyph Icons",
                        "icon" => "fa-plane",
                        "url" => "glyph.php"
                    )
                ) 
            ),
            "grid" => array(
                "title" => "Grid",
                "url" => "ajax/grid.php"
            ),
            "tree_view" => array(
                "title" => "Tree View",
                "url" => "ajax/treeview.php"
            ),
            "nestable_lists" => array(
                "title" => "Nestable Lists",
                "url" => "ajax/nestable-list.php"
            ),
            "jquery_ui" => array(
                "title" => "jQuery UI",
                "url" => "ajax/jqui.php"
            )
        )
    ),
	"nav6" => array(
		"title" => "6 Level Navigation",
		"icon" => "fa-folder-open",
		"sub" => array(
			"second_lvl" => array(
				"title" => "2nd Level",
				"icon" => "fa-folder-open",
				"sub" => array(
					"third_lvl" => array(
						"title" => "3rd Level",
						"icon" => "fa-folder-open",
						"sub" => array(
							"file" => array(
								"title" => "File",
								"icon" => "fa-file-text"
							),
							"fourth_lvl" => array(
								"title" => "4th Level",
								"icon" => "fa-folder-open",
								"sub" => array(
									"file" => array(
										"title" => "File",
										"icon" => "fa-file-text"
									),
									"fifth_lvl" => array(
										"title" => "5th Level",
										"icon" => "fa-folder-open",
										"sub" => array(
											"file" => array(
												"title" => "File",
												"icon" => "fa-file-text"
											),
											"file" => array(
												"title" => "File",
												"icon" => "fa-file-text"
											)
										)
									)
								)
							)
						)
					)
				)
			),
			"folder" => array(
				"title" => "Folder",
				"icon" => "fa-folder-open",
				"sub" => array(
					"third_lvl" => array(
						"title" => "3rd Level",
						"icon" => "fa-folder-open",
						"sub" => array(
							"file1" => array(
								"title" => "File",
								"icon" => "fa-file-text"
							),
							"file2" => array(
								"title" => "File",
								"icon" => "fa-file-text"
							)
						)
					)
				)
			)
		)
	),
    "cal" => array(
		"title" => "Calendar",
		"url" => "ajax/calendar.php",
		"icon" => "fa-calendar",
		"icon_badge" => "3"
	),
    "widgets" => array(
		"title" => "Widgets",
		"url" => "ajax/widgets.php",
		"icon" => "fa-list-alt"
	),
    "gallery" => array(
		"title" => "Gallery",
		"url" => "ajax/gallery.php",
		"icon" => "fa-picture-o"
	),
    "gmap_skins" => array(
		"title" => "Google Map Skins",
		"url" => "ajax/gmap-xml.php",
		"icon" => "fa-map-marker",
        "label_htm" => '<span class="badge bg-color-greenLight pull-right inbox-badge">9</span>'
	),
	"misc" => array(
		"title" => "Miscellaneous",
		"icon" => "fa-windows",
		"sub" => array(
            "typo" => array(
				"title" => "Typography",
				"url" => "ajax/typography.php"
			),
            "pricing_tables" => array(
				"title" => "Pricing Tables",
				"url" => "ajax/pricing-table.php"
			),
            "invoice" => array(
				"title" => "Invoice",
				"url" => "ajax/invoice.php"
			),
            "login" => array(
				"title" => "Login",
				"url" => APP_URL."/login.php",
				"ajax" => false
			),
            "register" => array(
				"title" => "Register",
				"url" => APP_URL."/register.php",
				"ajax" => false
			),
            "lock" => array(
				"title" => "Lock Screen",
				"url" => APP_URL."/lock.php",
				"ajax" => false
			),
            "err_404" => array(
				"title" => "Error 404",
				"url" => "ajax/error404.php"
			),
            "err_500" => array(
				"title" => "Error 500",
				"url" => "ajax/error500.php"
			),
			"blank" => array(
				"title" => "Blank Page",
				"icon" => "fa-file",
				"url" => "ajax/blank_.php"
			),
            "email_template" => array(
				"title" => "Email Template",
				"url" => "ajax/email-template.php"
			),
            "search" => array(
				"title" => "Search Page",
				"url" => "ajax/search.php"
			),
            "ck_editor" => array(
				"title" => "CK Editor",
				"url" => "ajax/ckeditor.php"
			),
		)
	),
    "others" => array(
        "title" => "Other Pages",
        "icon" => "fa-file",
        "sub" => array(
            "forum" => array(
                "title" => "Forum Layout",
                "url" => "ajax/forum.php"
            ),
            "profile" => array(
                "title" => "Profile",
                "url" => "ajax/profile.php"
            ),
            "timeline" => array(
                "title" => "Timeline",
                "url" => "ajax/timeline.php"
            )
        )
    )
);

//configuration variables
$page_title = "";
$page_css = array();
$no_main_header = false; //set true for lock.php and login.php
$page_body_prop = array(); //optional properties for <body>
?>