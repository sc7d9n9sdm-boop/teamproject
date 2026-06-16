import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import calendar
import random
import json
import os
import webbrowser



# ──────────────────────────────────────────
#  저장 파일 경로 (같은 폴더에 data.json 생성)
# ──────────────────────────────────────────
DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.json")

# ──────────────────────────────────────────
#  식당 목록 (restaurant_map.html 에서 추출)
# ──────────────────────────────────────────
RESTAURANTS = [
    {"name": "메밀꽃",       "type": "한식", "menu": "얼큰쫄순두부찌개", "price": 6500},
    {"name": "돈면가",       "type": "한식", "menu": "수제돈까스",        "price": 10000},
    {"name": "토천손칼국수", "type": "한식", "menu": "토천손칼국수",      "price": 7500},
    {"name": "울엄마손칼국시","type": "한식","menu": "얼큰닭칼국수",      "price": 9000},
    {"name": "승록이네",     "type": "한식", "menu": "닭떡볶이",          "price": 14000},
    {"name": "학교가는길",   "type": "한식", "menu": "치즈라볶이",        "price": 15000},
    {"name": "감자탕돈돈",   "type": "한식", "menu": "감자탕",            "price": 8000},
    {"name": "돼지세끼",     "type": "한식", "menu": "꽃삼겹",            "price": 16000},
    {"name": "the53",        "type": "한식", "menu": "돼지불백",          "price": 10000},
    {"name": "꼬장",         "type": "한식", "menu": "생삼겹",            "price": 13000},
    {"name": "김부삼",       "type": "한식", "menu": "급냉삼겹",          "price": 8500},
    {"name": "꼬밥",         "type": "한식", "menu": "우삽겹",            "price": 8000},
    {"name": "홍천식당",     "type": "한식", "menu": "제육",              "price": 6000},
    {"name": "소문난 곱창",   "type": "한식", "menu": "곱창야채볶음",      "price": 10000},
    {"name": "배불리찌개",   "type": "한식", "menu": "김치찌개",          "price": 10000},
    {"name": "손가",         "type": "한식", "menu": "매운국물콩나물갈비찜","price": 30000},
    {"name": "박지혜순대국",  "type": "한식","menu": "뼈없는 갈비탕",      "price": 14000},
    {"name": "육쌈냉면",     "type": "한식", "menu": "물냉면+숯불고기",   "price": 9500},
    {"name":"원조춘천숯불닭갈비","type":"한식","menu":"숯불닭갈비","price":15000},
     {"name":"탕화쿵푸마라탕","type":"중식","menu":"마라탕(2인)","price":20000},
    {"name": "남경", "type": "중식", "menu": "짜장면", "price": 7500},
    {"name": "북경", "type": "중식", "menu": "짜장면", "price": 7000},
    {"name": "면식당",       "type": "일식", "menu": "돈코츠라멘",        "price": 8400},
    {"name": "육회킹연어킹", "type": "일식", "menu": "육회덮밥",          "price": 7400},
    {"name": "스시마리오",   "type": "일식", "menu": "모듬스시",          "price": 16000},
    {"name": "나비루",       "type": "일식", "menu": "새꼬막덮밥",        "price": 10500},
    {"name": "멘야시오리",   "type": "일식", "menu": "아부라소바",        "price": 10500},
    {"name":"매화스시",     "type":"일식","menu":"오늘의초밥","price":16000},
    {"name":"신동랩","type":"일식","menu":"직화야끼토리동","price":7800},
    {"name":"쇼샤돈부리","type":"일식","menu":"스페셜돈","price":10500},
    {"name":"백소정","type":"일식","menu":"냉소바","price":9900},
    {"name":"오무야","type":"일식","menu":"새우투움바파스타","price":10900},
    {"name":"모야그집","type":"일식","menu":"가츠동","price":5900},
    {"name":"나의유부","type":"일식","menu":"나의한입유부","price":7500},
     {"name": "크라이치즈버거","type": "양식","menu": "치즈버거세트", "price": 8900},
    {"name": "마고피자", "type": "양식", "menu": "닭껍질피자", "price": 8900},
    {"name":"새우식탁", "type": "양식", "menu": "감바스알아히요", "price": 17000},
    {"name":"1983피자", "type": "양식", "menu": "백종원피자", "price": 16900},
    {"name":"버거리", "type": "양식", "menu": "트러플치즈버거", "price": 6600}, 
   ]

# ──────────────────────────────────────────
#  데이터 저장 / 불러오기
# ──────────────────────────────────────────
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# ──────────────────────────────────────────
#  메인 앱
# ──────────────────────────────────────────
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("🍚 밥약 도우미")
        self.root.geometry("560x700")
        self.root.resizable(False, False)
        self.show_main_screen()

    def clear(self):
        for w in self.root.winfo_children():
            w.destroy()

    # ── 메인 화면 ──────────────────────────
    def show_main_screen(self):
        self.clear()
        frame = tk.Frame(self.root, bg="#FFF8F0")
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text="🍚 밥약 도우미", font=("Arial", 22, "bold"),
                 bg="#FFF8F0", fg="#C0392B").pack(pady=40)
        tk.Label(frame, text="선배 ↔ 후배 밥약을 쉽게 잡아요!",
                 font=("Arial", 12), bg="#FFF8F0", fg="#555").pack(pady=5)

        tk.Button(frame, text="📅  약속 신청하기", font=("Arial", 14, "bold"),
                  bg="#E74C3C", fg="white", width=22, height=2,
                  relief="flat", cursor="hand2",
                  command=self.show_request_screen).pack(pady=20)

        tk.Button(frame, text="🔑  식별코드로 확인하기", font=("Arial", 14, "bold"),
                  bg="#2980B9", fg="white", width=22, height=2,
                  relief="flat", cursor="hand2",
                  command=self.show_lookup_screen).pack(pady=5)

    # ══════════════════════════════════════
    #  [약속 신청하기]
    # ══════════════════════════════════════
    def show_request_screen(self):
        self.clear()
        self.req_candidates = []
        self.req_year  = datetime.now().year
        self.req_month = datetime.now().month
        self.req_restaurants = [None, None, None]   # 1~3순위

        main = tk.Frame(self.root, bg="#FFF8F0")
        main.pack(fill="both", expand=True)

        # ── 상단 바 ──
        top = tk.Frame(main, bg="#C0392B")
        top.pack(fill="x")

        tk.Button(
			top,
			text="← 뒤로",
			bg="#C0392B",
			fg="white",
			relief="flat",
			font=("Arial", 10),
			command=self.show_main_screen
		).pack(side="left", padx=8, pady=6)

        tk.Label(
			top,
			text="약속 신청하기",
			font=("Arial", 13, "bold"),
			bg="#C0392B",
			fg="white"
		).pack(side="left")

		# ✅ 식당 지도 버튼 추가
        tk.Button(
			top,
			text="🗺 식당 지도",
			bg="#2980B9",
			fg="white",
			relief="flat",
			font=("Arial", 10),
			command=lambda: webbrowser.open(
				f"file://{os.path.abspath('restaurant_map.html')}"
			)
		).pack(side="right", padx=8, pady=6)

        # 스크롤 영역
        canvas = tk.Canvas(main, bg="#FFF8F0", highlightthickness=0)
        scrollbar = tk.Scrollbar(main, orient="vertical", command=canvas.yview)
        self.req_scroll = tk.Frame(canvas, bg="#FFF8F0")
        self.req_scroll.bind("<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=self.req_scroll, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        body = self.req_scroll

        # ── 이름 & 식별코드 ──
        sec = tk.LabelFrame(body, text=" 👤 내 정보 ", bg="#FFF8F0",
                            font=("Arial", 10, "bold"), padx=10, pady=8)
        sec.pack(fill="x", padx=15, pady=10)

        tk.Label(sec, text="이름:", bg="#FFF8F0", font=("Arial", 11)).grid(
            row=0, column=0, sticky="w")
        self.req_name_var = tk.StringVar()
        tk.Entry(sec, textvariable=self.req_name_var,
                 font=("Arial", 11), width=18).grid(row=0, column=1, padx=5)
        tk.Button(sec, text="식별코드 생성", bg="#E67E22", fg="white",
                  relief="flat", font=("Arial", 10),
                  command=self._gen_code).grid(row=0, column=2, padx=5)

        self.req_code_label = tk.Label(sec, text="식별코드: -",
                                       bg="#FFF8F0", font=("Arial", 11, "bold"),
                                       fg="#C0392B")
        self.req_code_label.grid(row=1, column=0, columnspan=3, pady=5, sticky="w")
        self.req_code = None

        # ── 달력 ──
        sec2 = tk.LabelFrame(body, text=" 📅 날짜 후보 추가 ", bg="#FFF8F0",
                             font=("Arial", 10, "bold"), padx=10, pady=8)
        sec2.pack(fill="x", padx=15, pady=5)

        nav = tk.Frame(sec2, bg="#FFF8F0")
        nav.pack()
        tk.Button(nav, text="<", command=self._req_prev_month,
                  width=3).pack(side="left")
        self.req_title_lbl = tk.Label(nav, text="", font=("Arial", 12, "bold"),
                                      bg="#FFF8F0", width=12)
        self.req_title_lbl.pack(side="left", padx=10)
        tk.Button(nav, text=">", command=self._req_next_month,
                  width=3).pack(side="left")

        self.req_cal_frame = tk.Frame(sec2, bg="#FFF8F0")
        self.req_cal_frame.pack()

        self.req_sel_day = tk.IntVar(value=0)
        self.req_sel_lbl = tk.Label(sec2, text="선택 날짜 없음",
                                    font=("Arial", 10), bg="#FFF8F0", fg="#555")
        self.req_sel_lbl.pack()

        time_f = tk.Frame(sec2, bg="#FFF8F0")
        time_f.pack(pady=4)
        tk.Label(time_f, text="시간:", bg="#FFF8F0").pack(side="left")
        self.req_hour = tk.Spinbox(time_f, from_=0, to=23, width=4,
                                   format="%02.0f")
        self.req_hour.pack(side="left", padx=2)
        tk.Label(time_f, text="시  분:", bg="#FFF8F0").pack(side="left")
        self.req_minute = tk.Spinbox(time_f, from_=0, to=59, width=4,
                                     format="%02.0f")
        self.req_minute.pack(side="left", padx=2)

        btn_f = tk.Frame(sec2, bg="#FFF8F0")
        btn_f.pack(pady=4)
        tk.Button(btn_f, text="+ 후보 추가", bg="#27AE60", fg="white",
                  relief="flat", command=self._req_add_candidate).pack(side="left", padx=4)
        tk.Button(btn_f, text="- 후보 삭제", bg="#95A5A6", fg="white",
                  relief="flat", command=self._req_del_candidate).pack(side="left", padx=4)

        self.req_listbox = tk.Listbox(sec2, height=5, font=("Arial", 10),
                                      width=38, selectbackground="#E74C3C")
        self.req_listbox.pack(pady=4)

        # ── 식당 선택 ──
        sec3 = tk.LabelFrame(body, text=" 🍽 식당 선택 ", bg="#FFF8F0",
                             font=("Arial", 10, "bold"), padx=10, pady=8)
        sec3.pack(fill="x", padx=15, pady=5)

        tk.Button(sec3, text="🎲 랜덤 추천", bg="#8E44AD", fg="white",
                  relief="flat", font=("Arial", 10),
                  command=self._req_random_rest).pack(pady=4)

        self.req_rest_labels = []
        for i in range(3):
            row_f = tk.Frame(sec3, bg="#FFF8F0")
            row_f.pack(fill="x", pady=2)
            tk.Label(row_f, text=f"{i+1}순위:", bg="#FFF8F0",
                     font=("Arial", 10, "bold"), width=6).pack(side="left")
            var = tk.StringVar(value="선택 안 됨")
            lbl = tk.Label(row_f, textvariable=var, bg="#FDEBD0",
                           font=("Arial", 10), width=20, relief="groove")
            lbl.pack(side="left", padx=4)
            tk.Button(row_f, text="선택", relief="flat", bg="#D5DBDB",
                      command=lambda idx=i: self._open_rest_picker(idx)).pack(side="left")
            self.req_rest_labels.append(var)

        # ── 저장 버튼 ──
        tk.Button(body, text="💾  저장하기", font=("Arial", 13, "bold"),
                  bg="#E74C3C", fg="white", relief="flat", width=20,
                  command=self._req_save).pack(pady=18)

        self._req_draw_calendar(self.req_year, self.req_month)

    # -- 식별코드 생성 --
    def _gen_code(self):
        name = self.req_name_var.get().strip()
        if not name:
            messagebox.showwarning("경고", "이름을 먼저 입력해주세요.")
            return
        code = f"N{random.randint(1000, 9999)}"
        self.req_code = code
        self.req_code_label.config(text=f"식별코드: {code}  ← 상대방에게 알려주세요!")

    # -- 달력 --
    def _req_draw_calendar(self, year, month):
        self.req_year, self.req_month = year, month
        for w in self.req_cal_frame.winfo_children():
            w.destroy()
        self.req_title_lbl.config(text=f"{year}년 {month}월")
        days = ["월","화","수","목","금","토","일"]
        for i, d in enumerate(days):
            tk.Label(self.req_cal_frame, text=d, width=4,
                     font=("Arial", 9, "bold"), bg="#FFF8F0").grid(row=0, column=i)
        for r, week in enumerate(calendar.monthcalendar(year, month), start=1):
            for c, day in enumerate(week):
                if day == 0:
                    continue
                tk.Button(self.req_cal_frame, text=str(day), width=4, height=1,
                          font=("Arial", 9),
                          command=lambda d=day: self._req_select_day(d)
                          ).grid(row=r, column=c, padx=1, pady=1)

    def _req_prev_month(self):
        m = self.req_month - 1
        y = self.req_year
        if m == 0: m, y = 12, y - 1
        self._req_draw_calendar(y, m)

    def _req_next_month(self):
        m = self.req_month + 1
        y = self.req_year
        if m == 13: m, y = 1, y + 1
        self._req_draw_calendar(y, m)

    def _req_select_day(self, day):
        self.req_sel_day.set(day)
        self.req_sel_lbl.config(
            text=f"선택: {self.req_year}-{self.req_month:02d}-{day:02d}")

    def _req_add_candidate(self):
        day = self.req_sel_day.get()
        if day == 0:
            messagebox.showwarning("경고", "날짜를 먼저 선택하세요."); return
        try:
            dt = datetime(self.req_year, self.req_month, day,
                          int(self.req_hour.get()), int(self.req_minute.get()))
        except ValueError:
            messagebox.showerror("오류", "올바른 날짜/시간이 아닙니다."); return
        if dt in self.req_candidates:
            messagebox.showwarning("중복", "이미 추가된 후보입니다."); return
        self.req_candidates.append(dt)
        self.req_listbox.insert(tk.END, dt.strftime("%Y-%m-%d %H:%M"))

    def _req_del_candidate(self):
        sel = self.req_listbox.curselection()
        if not sel:
            messagebox.showwarning("경고", "삭제할 항목을 선택하세요."); return
        i = sel[0]
        self.req_candidates.pop(i)
        self.req_listbox.delete(i)

    # -- 식당 선택 팝업 --
    def _open_rest_picker(self, rank_idx):
        win = tk.Toplevel(self.root)
        win.title(f"{rank_idx+1}순위 식당 선택")
        win.geometry("360x420")
        win.grab_set()

        tk.Label(win, text="식당을 선택하세요", font=("Arial", 12, "bold")).pack(pady=8)

        lb = tk.Listbox(win, height=16, font=("Arial", 10), width=40,
                        selectbackground="#E74C3C")
        lb.pack(padx=10)
        for r in RESTAURANTS:
            lb.insert(tk.END,
                      f"{r['name']}  ({r['type']})  대표: {r['menu']}  {r['price']:,}원")

        def confirm():
            sel = lb.curselection()
            if not sel:
                messagebox.showwarning("경고", "식당을 선택하세요.", parent=win); return
            chosen = RESTAURANTS[sel[0]]
            self.req_restaurants[rank_idx] = chosen
            self.req_rest_labels[rank_idx].set(
                f"{chosen['name']} ({chosen['type']})")
            win.destroy()

        tk.Button(win, text="선택 완료", bg="#E74C3C", fg="white",
                  relief="flat", font=("Arial", 11),
                  command=confirm).pack(pady=10)

    def _req_random_rest(self):
        chosen = random.sample(RESTAURANTS, min(3, len(RESTAURANTS)))
        for i, r in enumerate(chosen):
            self.req_restaurants[i] = r
            self.req_rest_labels[i].set(f"{r['name']} ({r['type']})")

    # -- 저장 --
    def _req_save(self):
        name = self.req_name_var.get().strip()
        if not name:
            messagebox.showwarning("경고", "이름을 입력해주세요."); return
        if not self.req_code:
            messagebox.showwarning("경고", "식별코드를 먼저 생성해주세요."); return
        if not self.req_candidates:
            messagebox.showwarning("경고", "날짜 후보를 1개 이상 추가해주세요."); return

        data = load_data()
        data[self.req_code] = {
            "name": name,
            "candidates": [dt.strftime("%Y-%m-%d %H:%M")
                           for dt in self.req_candidates],
            "restaurants": [
                {"name": r["name"], "type": r["type"],
                 "menu": r["menu"], "price": r["price"]}
                if r else None
                for r in self.req_restaurants
            ],
            "selected_datetime": None,
            "selected_restaurant": None,
        }
        save_data(data)
        messagebox.showinfo("저장 완료",
            f"저장되었습니다!\n\n식별코드: {self.req_code}\n\n"
            "상대방에게 이 코드를 알려주세요.")
        self.show_main_screen()

    # ══════════════════════════════════════
    #  [식별코드 입력하기]
    # ══════════════════════════════════════
    def show_lookup_screen(self):
        self.clear()
        main = tk.Frame(self.root, bg="#FFF8F0")
        main.pack(fill="both", expand=True)

        top = tk.Frame(main, bg="#2980B9")
        top.pack(fill="x")
        tk.Button(top, text="← 뒤로", bg="#2980B9", fg="white",
                  relief="flat", font=("Arial", 10),
                  command=self.show_main_screen).pack(side="left", padx=8, pady=6)
        tk.Label(top, text="식별코드로 확인하기",
                 font=("Arial", 13, "bold"),
                 bg="#2980B9", fg="white").pack(side="left")

        mid = tk.Frame(main, bg="#FFF8F0")
        mid.pack(expand=True)

        tk.Label(mid, text="식별코드를 입력하세요",
                 font=("Arial", 13, "bold"), bg="#FFF8F0").pack(pady=25)

        code_var = tk.StringVar()
        tk.Entry(mid, textvariable=code_var, font=("Arial", 14),
                 width=14, justify="center").pack(pady=8)

        def lookup():
            code = code_var.get().strip().upper()
            data = load_data()
            if code not in data:
                messagebox.showerror("오류",
                    f"'{code}' 코드를 찾을 수 없습니다.\n코드를 다시 확인해주세요.")
                return
            self.show_selection_screen(code, data[code])

        tk.Button(mid, text="확인", bg="#2980B9", fg="white",
                  relief="flat", font=("Arial", 13, "bold"),
                  width=12, command=lookup).pack(pady=12)

    # ══════════════════════════════════════
    #  [일정 선택 화면] – 식별코드 입력 후
    # ══════════════════════════════════════
    def show_selection_screen(self, code, record):
        self.clear()
        main = tk.Frame(self.root, bg="#FFF8F0")
        main.pack(fill="both", expand=True)

        top = tk.Frame(main, bg="#2980B9")
        top.pack(fill="x")
        tk.Button(top, text="← 뒤로", bg="#2980B9", fg="white",
                  relief="flat", font=("Arial", 10),
                  command=self.show_lookup_screen).pack(side="left", padx=8, pady=6)
        tk.Label(top, text="일정 선택",
                 font=("Arial", 13, "bold"),
                 bg="#2980B9", fg="white").pack(side="left")

        canvas = tk.Canvas(main, bg="#FFF8F0", highlightthickness=0)
        sb = tk.Scrollbar(main, orient="vertical", command=canvas.yview)
        body = tk.Frame(canvas, bg="#FFF8F0")
        body.bind("<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=body, anchor="nw")
        canvas.configure(yscrollcommand=sb.set)
        canvas.pack(side="left", fill="both", expand=True)
        sb.pack(side="right", fill="y")

        # 신청자 정보
        info = tk.LabelFrame(body, text=" 📋 신청 정보 ", bg="#FFF8F0",
                             font=("Arial", 10, "bold"), padx=10, pady=8)
        info.pack(fill="x", padx=15, pady=10)
        tk.Label(info, text=f"신청자: {record['name']}",
                 bg="#FFF8F0", font=("Arial", 11)).pack(anchor="w")
        tk.Label(info, text=f"식별코드: {code}",
                 bg="#FFF8F0", font=("Arial", 11), fg="#C0392B").pack(anchor="w")

        # 이미 최종 선택이 있으면 결과 표시
        if record.get("selected_datetime"):
            res = tk.LabelFrame(body, text=" ✅ 확정된 약속 ", bg="#E8F8F5",
                                font=("Arial", 10, "bold"), padx=10, pady=8)
            res.pack(fill="x", padx=15, pady=8)
            tk.Label(res, text=f"일시: {record['selected_datetime']}",
                     bg="#E8F8F5", font=("Arial", 12, "bold"),
                     fg="#1A5276").pack(anchor="w", pady=3)
            if record.get("selected_restaurant"):
                r = record["selected_restaurant"]
                tk.Label(res,
                    text=f"식당: {r['name']}  ({r['type']})  "
                         f"대표: {r['menu']}  {r['price']:,}원",
                    bg="#E8F8F5", font=("Arial", 11), fg="#1A5276").pack(anchor="w")
            return   # 이미 확정된 경우 선택 UI 표시 안 함

        # ── 날짜 후보 선택 ──
        sec = tk.LabelFrame(body, text=" 📅 날짜 후보 선택 ", bg="#FFF8F0",
                            font=("Arial", 10, "bold"), padx=10, pady=8)
        sec.pack(fill="x", padx=15, pady=8)
        tk.Label(sec, text="원하는 날짜를 선택하세요:",
                 bg="#FFF8F0", font=("Arial", 10)).pack(anchor="w")

        date_var = tk.StringVar()
        for dt_str in record["candidates"]:
            tk.Radiobutton(sec, text=dt_str, variable=date_var, value=dt_str,
                           bg="#FFF8F0", font=("Arial", 11),
                           activebackground="#FDEBD0").pack(anchor="w", pady=2)

        # ── 식당 후보 표시 ──
        sec2 = tk.LabelFrame(body, text=" 🍽 식당 후보 ", bg="#FFF8F0",
                             font=("Arial", 10, "bold"), padx=10, pady=8)
        sec2.pack(fill="x", padx=15, pady=8)

        rest_var = tk.StringVar()
        valid_rests = [(i, r) for i, r in enumerate(record["restaurants"]) if r]
        if valid_rests:
            for i, r in valid_rests:
                label = f"{i+1}순위 | {r['name']} ({r['type']}) | {r['menu']} {r['price']:,}원"
                tk.Radiobutton(sec2, text=label,
                               variable=rest_var, value=r["name"],
                               bg="#FFF8F0", font=("Arial", 10),
                               activebackground="#FDEBD0").pack(anchor="w", pady=2)
        else:
            tk.Label(sec2, text="식당 후보 없음", bg="#FFF8F0",
                     font=("Arial", 10), fg="#999").pack()

        # ── 최종 확정 버튼 ──
        def confirm():
            if not date_var.get():
                messagebox.showwarning("경고", "날짜를 선택해주세요."); return

            # 선택된 식당 찾기
            sel_rest = None
            for i, r in valid_rests:
                if r and r["name"] == rest_var.get():
                    sel_rest = r
                    break

            data = load_data()
            data[code]["selected_datetime"] = date_var.get()
            data[code]["selected_restaurant"] = sel_rest
            save_data(data)

            # 최종 신청서 팝업
            win = tk.Toplevel(self.root)
            win.title("✅ 최종 신청서")
            win.geometry("380x280")
            win.grab_set()
            tk.Label(win, text="🎉 약속이 확정되었습니다!",
                     font=("Arial", 14, "bold"), fg="#1A5276").pack(pady=20)
            tk.Label(win, text=f"신청자: {record['name']}",
                     font=("Arial", 12)).pack()
            tk.Label(win, text=f"일시: {date_var.get()}",
                     font=("Arial", 12, "bold"), fg="#C0392B").pack(pady=4)
            if sel_rest:
                tk.Label(win,
                    text=f"식당: {sel_rest['name']} ({sel_rest['type']})\n"
                         f"대표메뉴: {sel_rest['menu']}  {sel_rest['price']:,}원",
                    font=("Arial", 11)).pack(pady=4)
            tk.Button(win, text="확인", bg="#2980B9", fg="white",
                      relief="flat", font=("Arial", 11),
                      command=lambda: [win.destroy(),
                                       self.show_main_screen()]).pack(pady=16)

        tk.Button(body, text="✅  이 일정으로 확정하기",
                  font=("Arial", 12, "bold"),
                  bg="#2980B9", fg="white", relief="flat", width=24,
                  command=confirm).pack(pady=18)


# ──────────────────────────────────────────
#  실행
# ──────────────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()