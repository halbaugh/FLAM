#QTCSS


splitterCSS = """
            QSplitter::handle {
                background-color: rgb(65, 65, 65);
            }

            QSplitter::handle:horizontal {
                width: 10px;
            }

            QSplitter::handle:vertical {
                height: 10px;
            }

            QSplitter::handle:pressed {
                image: url(images/splitter_pressed.png);
            }
            """


menubarCSS = """
            QMenuBar {
                background-color: rgb(60, 60, 60);
                color: rgb(255,255,255);
                border: 1px solid #000;
            }

            QMenuBar::item {
                background-color: rgb(60, 60, 60);
                color: rgb(255,255,255);
            }

            QMenuBar::item::selected {
                background-color: rgb(100, 100, 100);
            }

            QMenu {
                background-color: rgb(60, 60, 60);
                color: rgb(255,255,255);
                border: 1px solid #000;           
            }

            QMenu::item::selected {

                background-color: rgb(100, 100, 100);
            }
            """


showComboBoxCSS = """
                QComboBox {
                    border: 1px solid rgb(110, 110, 110);
                    border-radius: 3px;
                    padding: 1px 18px 1px 3px;
                    min-width: 6em;
                    background: rgb(255, 100, 100);
                }

                QComboBox:hover
                {
                    border: 1px solid rgb(150, 150, 150);

                }

                QComboBox:editable {
                    background: red;

                }

                QComboBox:!editable, QComboBox::drop-down:editable {
                     background: rgb(100, 100, 100);
                }

                /* QComboBox gets the "on" state when the popup is open */
                QComboBox:!editable:on, QComboBox::drop-down:editable:on {
                    background: rgb(100, 100, 100);
                }

                QComboBox:on { /* shift the text when the popup opens */
                    padding-top: 3px;
                    padding-left: 4px;
                }

                QComboBox::drop-down {
                    subcontrol-origin: padding;
                    subcontrol-position: top right;
                    width: 15px;
                    background: rgb(100, 100, 100);
                    border-left-width: 1px;
                    border-left-color: rgb(100, 100, 100);
                    border-left-style: solid; /* just a single line */
                    border-top-right-radius: 3px; /* same radius as the QComboBox */
                    border-bottom-right-radius: 3px;
                }

                QComboBox::down-arrow {
                    image: 'icons/downArrow.png';
                }

                QComboBox::down-arrow:on { /* shift the arrow when popup is open */
                    top: 1px;
                    left: 1px;
                }

                QComboBox QAbstractItemView
                {
                    border: 1px solid rgb(100,100,100);
                    color: rgb(200,200,200);
                    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #111, stop: 1 #333);
                }
                """